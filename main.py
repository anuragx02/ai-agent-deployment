from fastapi import FastAPI, HTTPException, Request
from dotenv import load_dotenv
import os
import logging
from armoriq_sdk import ArmorIQClient
from armoriq_sdk.exceptions import (
    InvalidTokenException,
    IntentMismatchException,
    MCPInvocationException,
    TokenExpiredException,
)
import os as os_sys
from fastapi.responses import StreamingResponse
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
from typing import Dict, Any

load_dotenv(
    dotenv_path=os_sys.path.join(os_sys.path.dirname(__file__), ".env"),
    override=True,
)

logger = logging.getLogger("mcp")

def _required_env(name: str) -> str:
    value = (os.getenv(name) or "").strip()
    if not value:
        raise RuntimeError(f"Missing {name} in .env.")
    return value

api_key = _required_env("ARMORIQ_API_KEY")
user_id = _required_env("ARMORIQ_USER_ID")
agent_id = _required_env("ARMORIQ_AGENT_ID")
sdk_timeout = float(os.getenv("ARMORIQ_TIMEOUT_SECONDS", "120"))

app = FastAPI()

client = ArmorIQClient(
    api_key=api_key,
    user_id=user_id,
    agent_id=agent_id,
    timeout=sdk_timeout,
)

BASE_DIR = "workspace"
os_sys.makedirs(BASE_DIR, exist_ok=True)

# -------------------
# REAL MCP SERVER (JSON-RPC + SSE)
# -------------------

TOOLS = [
    {
        "name": "list_files",
        "description": "List files inside workspace directory",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]

def sse_response(data):
    return f"event: message\ndata: {json.dumps(data)}\n\n"

async def handle_jsonrpc(request_data):
    method = request_data.get("method")
    msg_id = request_data.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {
                        "listChanged": False
                    }
                },
                "serverInfo": {
                    "name": "filesystem-mcp",
                    "version": "1.0.0"
                }
            }
        }

    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "tools": TOOLS
            }
        }

    elif method in {"tools/call", "tool/call"}:
        params = request_data.get("params", {})
        tool_name = params.get("name") or params.get("tool") or params.get("action")

        if tool_name == "list_files":
            files = os_sys.listdir(BASE_DIR)

            result_data = {"files": files}

            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result_data)
                        }
                    ]
                }
            }
    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": "Method not found"}
    }

class MCPRequest(BaseModel):
    jsonrpc: str
    id: int | str | None
    method: str
    params: Dict[str, Any] | None = None

@app.post("/mcp")
async def mcp_endpoint(request: Request):
    try:
        body = await request.json()
    except Exception:
        raw_body = await request.body()
        if not raw_body:
            raise HTTPException(status_code=400, detail="Missing JSON body.")
        try:
            body = json.loads(raw_body.decode("utf-8"))
        except json.JSONDecodeError as exc:
            raise HTTPException(status_code=400, detail="Invalid JSON body.") from exc

    if isinstance(body, str):
        try:
            body = json.loads(body)
        except json.JSONDecodeError as exc:
            raise HTTPException(status_code=400, detail="Invalid JSON body.") from exc

    if not isinstance(body, dict):
        raise HTTPException(status_code=400, detail="JSON body must be an object.")

    if os.getenv("ARMORIQ_MCP_DEBUG", "").lower() in {"1", "true", "yes", "on"}:
        logger.info("MCP request: %s", json.dumps(body, ensure_ascii=True))

    try:
        request_model = MCPRequest(**body)
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Invalid MCP request.") from exc

    response_data = await handle_jsonrpc(request_model.dict())

    if os.getenv("ARMORIQ_MCP_DEBUG", "").lower() in {"1", "true", "yes", "on"}:
        logger.info("MCP response: %s", json.dumps(response_data, ensure_ascii=True))

    accept_header = (request.headers.get("accept") or "").lower()
    if "application/json" not in accept_header and "text/event-stream" in accept_header:
        async def stream():
            json_str = json.dumps(response_data)
            yield f"event: message\ndata: {json_str}\n\n"

        return StreamingResponse(stream(), media_type="text/event-stream")

    return JSONResponse(response_data)

# -------------------
# HEALTH CHECK
# -------------------

@app.get("/")
async def root():
    return {"status": "ok"}

@app.get("/health")
async def health():
    return {"status": "healthy"}


# -------------------
# AGENT ROUTE
# -------------------

class AgentRequest(BaseModel):
    instruction: str

@app.post("/agent")
async def agent(req: AgentRequest):
    instruction = req.instruction

    plan = {
        "goal": instruction,
        "steps": [
            {
                "action": "list_files",
                "mcp": "filesystem-mcp",
                "params": {}
            }
        ]
    }

    try:
        captured = client.capture_plan(
            llm="hardcoded",
            prompt=instruction,
            plan=plan
        )

        token = client.get_intent_token(captured)
        step = plan["steps"][0]

        result = client.invoke(
            mcp=step["mcp"],
            action=step["action"],
            intent_token=token,
            params=step["params"]
        )
        return result
    except TokenExpiredException as e:
        raise HTTPException(status_code=401, detail=str(e))
    except (InvalidTokenException, IntentMismatchException) as e:
        raise HTTPException(status_code=400, detail=str(e))
    except MCPInvocationException as e:
        raise HTTPException(
            status_code=504,
            detail=f"MCP invocation timeout/failure: {str(e)}"
        )
