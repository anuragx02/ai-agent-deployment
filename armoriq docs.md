\# Installation

Installation \[\#installation\]

Requirements \[\#requirements\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \* Python 3.8 or higher  
    \* pip 20.0 or higher  
    \* HTTPS-capable network connection  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \* Node.js 18 or higher  
    \* npm 8.0 or higher  
    \* HTTPS-capable network connection  
  \</Tab\>  
\</Tabs\>

Install from Package Manager \[\#install-from-package-manager\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`bash  
    pip install armoriq-sdk  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`bash  
    npm install @armoriq/sdk  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Verify Installation \[\#verify-installation\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    import armoriq\_sdk  
    print(armoriq\_sdk.\_\_version\_\_) \# Should print: 1.0.0  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import { VERSION } from '@armoriq/sdk';  
    console.log(VERSION); // Should print: 0.2.6  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

\# Client Initialization

Client Initialization \[\#client-initialization\]

ArmorIQClient \[\#armoriqclient\]

The main entry point for interacting with ArmorIQ.

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    from armoriq\_sdk import ArmorIQClient  
    client \= ArmorIQClient(  
        api\_key: str \= None,  
        user\_id: str \= None,  
        agent\_id: str \= None,  
        proxy\_url: str \= None,  
        timeout: int \= 30,  
        max\_retries: int \= 3,  
        verify\_ssl: bool \= True  
    )  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import { ArmorIQClient } from '@armoriq/sdk';

    const client \= new ArmorIQClient({  
      apiKey: string,           // Required  
      userId: string,           // Required  
      agentId: string,          // Required  
      proxyEndpoint?: string,   // Optional  
      timeout?: number,         // Optional (default: 30000ms)  
      maxRetries?: number,      // Optional (default: 3\)  
      verifySsl?: boolean       // Optional (default: true)  
    });  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Parameters \[\#parameters\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    | Parameter    | Type | Required | Default                                                                | Description                                                              |  
    | \------------ | \---- | \-------- | \---------------------------------------------------------------------- | \------------------------------------------------------------------------ |  
    | api\\\_key     | str  | Yes      | ARMORIQ\\\_API\\\_KEY env var                                              | Your API key (format: \`ak\_live\_\` \+ 64 hex characters)                    |  
    | user\\\_id     | str  | Yes      | ARMORIQ\\\_USER\\\_ID env var                                              | User identifier for tracking (you can define your own unique identifier) |  
    | agent\\\_id    | str  | Yes      | ARMORIQ\\\_AGENT\\\_ID env var                                             | Unique agent identifier (you can define your own unique identifier)      |  
    | proxy\\\_url   | str  | No       | \[https://customer-proxy.armoriq.ai\](https://customer-proxy.armoriq.ai) | ArmorIQ Proxy base URL                                                   |  
    | timeout      | int  | No       | 30                                                                     | Request timeout in seconds                                               |  
    | max\\\_retries | int  | No       | 3                                                                      | Max retry attempts for failed requests                                   |  
    | verify\\\_ssl  | bool | No       | True                                                                   | Verify SSL certificates                                                  |  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    | Parameter     | Type    | Required | Default                                                                | Description                                                              |  
    | \------------- | \------- | \-------- | \---------------------------------------------------------------------- | \------------------------------------------------------------------------ |  
    | apiKey        | string  | Yes      | ARMORIQ\\\_API\\\_KEY env var                                              | Your API key (format: \`ak\_live\_\` \+ 64 hex characters)                    |  
    | userId        | string  | Yes      | USER\\\_ID env var                                                       | User identifier for tracking (you can define your own unique identifier) |  
    | agentId       | string  | Yes      | AGENT\\\_ID env var                                                      | Unique agent identifier (you can define your own unique identifier)      |  
    | proxyEndpoint | string  | No       | \[https://customer-proxy.armoriq.ai\](https://customer-proxy.armoriq.ai) | ArmorIQ Proxy base URL                                                   |  
    | timeout       | number  | No       | 30000                                                                  | Request timeout in milliseconds                                          |  
    | maxRetries    | number  | No       | 3                                                                      | Max retry attempts for failed requests                                   |  
    | verifySsl     | boolean | No       | true                                                                   | Verify SSL certificates                                                  |  
  \</Tab\>  
\</Tabs\>

Environment Variables \[\#environment-variables\]

It's recommended to set these variables in your development environment:

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`bash  
    \# Required  
    export ARMORIQ\_API\_KEY="ak\_live\_..."  
    export ARMORIQ\_USER\_ID="your\_unique\_user\_id"      \# Define your own unique identifier  
    export ARMORIQ\_AGENT\_ID="your\_unique\_agent\_id"    \# Define your own unique identifier

    \# Optional  
    export ARMORIQ\_PROXY\_URL="https://customer-proxy.armoriq.ai"  
    export ARMORIQ\_TIMEOUT="30"  
    export ARMORIQ\_MAX\_RETRIES="3"  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`bash  
    \# Required  
    export ARMORIQ\_API\_KEY="ak\_live\_..."  
    export USER\_ID="your\_unique\_user\_id"      \# Define your own unique identifier  
    export AGENT\_ID="your\_unique\_agent\_id"    \# Define your own unique identifier

    \# Optional  
    export PROXY\_ENDPOINT="https://customer-proxy.armoriq.ai"  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Returns \[\#returns\]

ArmorIQClient instance

Raises \[\#raises\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \* ValueError: If required parameters are missing  
    \* InvalidAPIKeyError: If API key format is invalid  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \* ConfigurationException: If required parameters are missing or API key format is invalid  
  \</Tab\>  
\</Tabs\>

Example \[\#example\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    import os  
    from armoriq\_sdk import ArmorIQClient

    \# Using environment variables (recommended)  
    client \= ArmorIQClient()

    \# Explicit parameters  
    client \= ArmorIQClient(  
        api\_key="ak\_live\_" \+ "a" \* 64,  
        user\_id="user\_12345",  
        agent\_id="analytics\_bot\_v1",  
        proxy\_url="https://customer-proxy.armoriq.ai",  
        timeout=60  
    )

    \# Custom configuration  
    client \= ArmorIQClient(  
        api\_key=os.getenv("ARMORIQ\_API\_KEY"),  
        user\_id=get\_current\_user\_id(),  
        agent\_id=f"agent\_{uuid.uuid4()}",  
        max\_retries=5  
    )  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import { ArmorIQClient } from '@armoriq/sdk';

    // Using environment variables (recommended)  
    const client \= new ArmorIQClient({  
      apiKey: process.env.ARMORIQ\_API\_KEY\!,  
      userId: process.env.USER\_ID\!,  
      agentId: process.env.AGENT\_ID\!  
    });

    // Explicit parameters  
    const client \= new ArmorIQClient({  
      apiKey: 'ak\_live\_' \+ 'a'.repeat(64),  
      userId: 'user\_12345',  
      agentId: 'analytics\_bot\_v1',  
      proxyEndpoint: 'https://customer-proxy.armoriq.ai',  
      timeout: 60000  
    });

    // With production mode disabled (for local development)  
    const client \= new ArmorIQClient({  
      apiKey: process.env.ARMORIQ\_API\_KEY\!,  
      userId: 'demo-user',  
      agentId: 'demo-agent',  
      useProduction: false  // Use local development endpoints  
    });  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

\# What is ArmorIQ?

What is ArmorIQ? \[\#what-is-armoriq\]

ArmorIQ is a \*\*security platform for AI agents\*\* that enables cryptographically verified action execution across multiple services. Think of it as a \*\*zero-trust security layer\*\* specifically designed for LLM-powered agents.

The Problem We Solve \[\#the-problem-we-solve\]

Traditional AI agents face critical security challenges:

\* \*\*Prompt Injection Attacks\*\*: Malicious prompts can trick agents into executing unauthorized actions  
\* \*\*Agent Drift\*\*: Agents can deviate from intended behavior during execution  
\* \*\*Lack of Auditability\*\*: No clear trail of what the agent planned vs. what it executed  
\* \*\*Unauthorized Escalation\*\*: Compromised agents can access services beyond their scope

The ArmorIQ Solution \[\#the-armoriq-solution\]

ArmorIQ bridges two worlds:

1\. \*\*AI Agents\*\* that use LLMs to reason and plan dynamically  
2\. \*\*Zero-Trust Security\*\* that cryptographically verifies every action

Traditional Approach \[\#traditional-approach\]

\`\`\`python  
\# Direct calls \- no verification  
api.call("service1", "action1")  
api.call("service2", "action2")  
api.call("service3", "action3")  \# Could be malicious\!  
\`\`\`

ArmorIQ Approach \[\#armoriq-approach\]

\`\`\`python  
\# Step 1: Agent captures intent (LLM generates plan)  
captured\_plan \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Fetch sales data and analyze Q4 performance"  
)  
\# LLM decides: data-mcp/fetch\_sales → analytics-mcp/analyze

\# Step 2: Get cryptographic proof for the LLM-generated plan  
token \= client.get\_intent\_token(captured\_plan)

\# Step 3: Only declared actions can execute  
client.invoke(  
    mcp="data-mcp",  
    action="fetch\_sales",  
    intent\_token=token,  
    params={...}  
)   \# ✓ Verified (in plan)

client.invoke(  
    mcp="analytics-mcp",  
    action="analyze",  
    intent\_token=token,  
    params={...}  
)  \# ✓ Verified (in plan)

client.invoke(  
    mcp="data-mcp",  
    action="delete\_all",  
    intent\_token=token,  
    params={...}  
)    \# ✗ Fails \- LLM didn't plan this\!  
\`\`\`

Key Insights \[\#key-insights\]

\*\*Even though the LLM generated the plan dynamically, every action is cryptographically verified.\*\* This prevents:

\* \*\*Prompt injection attacks\*\*: Malicious prompts can't execute unplanned actions  
\* \*\*Agent drift\*\*: Agent can't deviate from captured intent  
\* \*\*Unauthorized escalation\*\*: Even if compromised, agent is bound to the plan

Core Principles \[\#core-principles\]

1\. Intent-Based Execution \[\#1-intent-based-execution\]

Instead of directly calling services, you declare your \*\*intent\*\* (what you want to do) upfront. This intent becomes a cryptographically verified contract.

2\. Zero Trust Security \[\#2-zero-trust-security\]

ArmorIQ follows zero trust principles:

\* Every action is verified cryptographically  
\* Tokens are time-limited and non-reusable  
\* Plans are immutable once signed  
\* All requests are authenticated  
\* Complete audit trail maintained

3\. LLM-Generated Plans \[\#3-llm-generated-plans\]

Plans are \*\*declarative\*\* and \*\*LLM-generated\*\*, not manually coded:

\`\`\`python  
\# ✓ Agent captures intent from natural language  
captured\_plan \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Fetch user data and calculate credit score"  
)  
\# LLM generates declarative plan:  
\# \[  
\#   {"action": "fetch\_data", "mcp": "data-mcp"},  
\#   {"action": "calculate\_score", "mcp": "analytics-mcp"}  
\# \]  
\`\`\`

\*\*Why This Matters:\*\*

\* \*\*LLM Autonomy\*\*: Agent decides the best approach based on prompt  
\* \*\*Cryptographic Binding\*\*: Even dynamic plans are immutably verified  
\* \*\*Declarative Security\*\*: You secure what the agent wants, not how it does it  
\* \*\*No Implementation Details\*\*: MCPs handle the how, plans declare the what

Next Steps \[\#next-steps\]

\* \[Architecture Overview\](./architecture) \- Understand the system components  
\* \[Intent Plans\](./intent-plans) \- Learn about plan structure and lifecycle  
\* \[Security Model\](./security-model) \- Deep dive into security mechanisms  
\* \[Token Lifecycle\](./token-lifecycle) \- How tokens work

\# Architecture Overview

Architecture Overview \[\#architecture-overview\]

ArmorIQ uses a \*\*proxy-based architecture\*\* where all agent requests flow through a secure verification layer before reaching MCP servers.

System Components \[\#system-components\]

| Component         | Purpose                                                                           |  
| \----------------- | \--------------------------------------------------------------------------------- |  
| \*\*ArmorIQ SDK\*\*   | Client library that enables agents to securely connect and interact with services |  
| \*\*ArmorIQ API\*\*   | Token generation and plan validation service                                      |  
| \*\*ArmorIQ Proxy\*\* | Security gateway that verifies and routes requests                                |  
| \*\*MCP Servers\*\*   | Service providers that execute specific actions (data, analytics, etc.)           |  
| \*\*MCP Registry\*\*  | Catalog of available services and their supported actions                         |

Request Flow \[\#request-flow\]

1\. Plan Capture \[\#1-plan-capture\]

\`\`\`python  
captured\_plan \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Fetch sales data and analyze"  
)  
\`\`\`

\*\*Flow:\*\*

\* SDK sends plan to ArmorIQ API  
\* API validates plan structure against registry  
\* Canonical representation created  
\* Plan stored with unique ID  
\* Plan details returned to agent

2\. Token Generation \[\#2-token-generation\]

\`\`\`python  
token \= client.get\_intent\_token(  
    plan\_capture=captured\_plan,  
    policy={"allow": \["\*"\], "deny": \[\]}  
)  
\`\`\`

\*\*Flow:\*\*

\* SDK sends plan \+ policy to ArmorIQ API  
\* API verifies plan structure  
\* Canonical plan hash generated  
\* Token cryptographically signed with:  
  \* Plan hash  
  \* Policy constraints  
  \* Expiration time  
  \* User/agent identity  
\* Signed token returned to agent

3\. Action Execution \[\#3-action-execution\]

\`\`\`python  
result \= client.invoke(  
    mcp="data-mcp",  
    action="fetch\_data",  
    intent\_token=token,  
    params={"query": "sales"}  
)  
\`\`\`

\*\*Flow:\*\*

\* SDK sends request to ArmorIQ Proxy with token and Merkle proof  
\* Proxy verifies:  
  \* Ed25519 signature validity  
  \* Merkle proof of action in plan  
  \* Policy constraints  
  \* Token expiration  
  \* Rate limits  
\* If verified, request forwarded to MCP  
\* MCP response returned to agent with signature  
\* Audit log created

Security Layers \[\#security-layers\]

Layer 1: Authentication \[\#layer-1-authentication\]

\* API key validation  
\* User identity verification  
\* Agent identification

Layer 2: Authorization (Policy) \[\#layer-2-authorization-policy\]

\* Action allowlist/denylist  
\* Time-based restrictions  
\* IP whitelisting  
\* Rate limiting

Layer 3: Intent Verification \[\#layer-3-intent-verification\]

\* Token signature validation  
\* Plan hash verification  
\* Merkle proof validation  
\* Action-plan matching  
\* Token expiration check

Layer 4: Audit Trail \[\#layer-4-audit-trail\]

\* Complete request logging  
\* Plan history tracking  
\* Token usage monitoring  
\* Anomaly detection

Component Details \[\#component-details\]

ArmorIQ API \[\#armoriq-api\]

\*\*Responsibilities:\*\*

\* Token generation and signing  
\* Plan canonicalization  
\* Plan validation  
\* Cryptographic operations

ArmorIQ Proxy \[\#armoriq-proxy\]

\*\*Responsibilities:\*\*

\* Request gateway and routing  
\* Token signature verification  
\* Merkle proof verification  
\* Policy enforcement  
\* Rate limiting  
\* Audit logging

MCP Servers \[\#mcp-servers\]

\*\*Responsibilities:\*\*

\* Execute specific business logic  
\* Return structured results  
\* Follow MCP protocol standards

MCP Registry \[\#mcp-registry\]

\*\*Responsibilities:\*\*

\* Service discovery  
\* Action catalog  
\* Schema validation  
\* Version management

Complete Agent Flow \[\#complete-agent-flow\]

Here's how a complete agent interaction works from user input to result:

\<img alt="Complete Agent Flow" src={\_\_img0} placeholder="blur" /\>

Flow Explanation \[\#flow-explanation\]

\*\*Planning Phase:\*\*

1\. User sends message to agent backend  
2\. Backend streams request to LLM provider  
3\. LLM determines required tool calls (e.g., "loan\\\_calculator")  
4\. Backend calls \`capture\_plan()\` with tool calls  
5\. SDK sends plan to ArmorIQ API for token generation  
6\. API validates plan and returns signed IntentToken  
7\. Backend receives token for execution

\*\*Execution Phase:\*\*

1\. Backend calls \`invoke()\` with action and token  
2\. SDK sends request to Proxy with token and Merkle proof  
3\. Proxy performs three-step verification:  
   \* Verifies Ed25519 signature  
   \* Validates Merkle proof (action in plan)  
   \* Enforces policy constraints  
4\. Proxy forwards request to appropriate MCP server  
5\. MCP executes action and returns result  
6\. Proxy signs result and returns to SDK  
7\. SDK returns result to backend  
8\. Backend streams result to user

Deployment Architecture \[\#deployment-architecture\]

Cloud Deployment \[\#cloud-deployment\]

\`\`\`  
Load Balancer  
   │  
   ├──▶ API Instance (Token Generation)  
   │  
   ├──▶ Proxy Instances (Request Verification)  
   │     └── Connects to MCP Servers  
   │  
   └──▶ Database (Plans, Tokens, Audit Logs)  
\`\`\`

Scalability \[\#scalability\]

ArmorIQ is designed for horizontal scaling:

\* \*\*Stateless Services\*\*: Add more instances as needed  
\* \*\*Token Caching\*\*: Reduce token generation load  
\* \*\*Distributed Verification\*\*: Multiple proxy instances  
\* \*\*Load Balancing\*\*: Distribute requests evenly

Next Steps \[\#next-steps\]

\* \[Intent Plans\](./intent-plans) \- Learn about plan structure  
\* \[Security Model\](./security-model) \- Deep dive into security  
\* \[Token Lifecycle\](./token-lifecycle) \- How tokens work

\# Intent Plans

Intent Plans \[\#intent-plans\]

An \*\*Intent Plan\*\* is a structured document that declares all actions an agent intends to execute. Think of it as a "pre-approved checklist" that gets cryptographically signed.

What is an Intent Plan? \[\#what-is-an-intent-plan\]

An intent plan is:

\* \*\*Declarative\*\*: States what to do, not how  
\* \*\*LLM-Generated\*\*: Created dynamically by the agent's reasoning  
\* \*\*Immutable\*\*: Cannot be changed once signed  
\* \*\*Verifiable\*\*: Cryptographically bound to execution

Plan Structure \[\#plan-structure\]

Basic Plan Format \[\#basic-plan-format\]

\`\`\`json  
{  
  "steps": \[  
    {  
      "action": "fetch\_data",  
      "mcp": "data-mcp",  
      "description": "Get user data from database"  
    },  
    {  
      "action": "analyze",  
      "mcp": "analytics-mcp",  
      "description": "Calculate risk score"  
    }  
  \]  
}  
\`\`\`

Plan with Metadata \[\#plan-with-metadata\]

\`\`\`json  
{  
  "steps": \[  
    {  
      "action": "process\_payment",  
      "mcp": "finance-mcp",  
      "description": "Process customer payment",  
      "metadata": {  
        "priority": "high",  
        "timeout\_seconds": 30  
      }  
    }  
  \],  
  "metadata": {  
    "purpose": "payment\_processing",  
    "version": "1.2.0",  
    "tags": \["finance", "critical"\]  
  }  
}  
\`\`\`

Plan Templates vs LLM Generation \[\#plan-templates-vs-llm-generation\]

Primary: LLM-Generated Plans (Recommended) \[\#primary-llm-generated-plans-recommended\]

\`\`\`python  
\# Agent uses LLM to generate plan from natural language  
captured \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Fetch user data, calculate credit score, and store result"  
)  
\# LLM autonomously decides which MCPs and actions to use  
\`\`\`

\*\*Benefits:\*\*

\* Maximum flexibility  
\* Agent autonomy  
\* Adapts to context  
\* Natural language interface

Alternative: Plan Templates (Fixed Structure) \[\#alternative-plan-templates-fixed-structure\]

\`\`\`python  
\# For debugging, testing, or strict workflows  
plan\_template \= {  
    "steps": \[  
        {"action": "fetch\_data", "mcp": "data-mcp"},  
        {"action": "analyze", "mcp": "analytics-mcp"}  
    \]  
}

captured \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Execute predefined workflow",  
    plan=plan\_template  \# Use fixed structure  
)  
\`\`\`

\*\*Use Cases:\*\*

\* Testing and debugging  
\* Regulatory compliance (fixed workflows)  
\* Performance-critical scenarios (skip LLM planning)  
\* Template-based execution

\*\*Note:\*\* Plan templates are more restrictive than LLM-generated plans. They're useful for specific scenarios but sacrifice agent flexibility.

Plan Validation \[\#plan-validation\]

When you submit a plan, ArmorIQ validates:

1\. Structure Validation \[\#1-structure-validation\]

\*\*Checks:\*\*

\* Required fields present (\`action\`, \`mcp\`)  
\* Field types correct (strings, objects)  
\* No malformed JSON  
\* Valid step ordering

\*\*Example Error:\*\*

\`\`\`json  
{  
  "error": "InvalidPlanError",  
  "message": "Step 2 missing required field: 'action'",  
  "details": {  
    "step\_index": 2,  
    "missing\_fields": \["action"\]  
  }  
}  
\`\`\`

2\. MCP Validation \[\#2-mcp-validation\]

\*\*Checks:\*\*

\* MCP exists in registry  
\* Action is supported by MCP  
\* Action schema matches  
\* MCP is accessible to user/agent

\*\*Example Error:\*\*

\`\`\`json  
{  
  "error": "InvalidMCPError",  
  "message": "MCP 'unknown-mcp' not found in registry",  
  "details": {  
    "requested\_mcp": "unknown-mcp",  
    "available\_mcps": \["data-mcp", "analytics-mcp", "finance-mcp"\]  
  }  
}  
\`\`\`

Plan Lifecycle \[\#plan-lifecycle\]

Phase 1: Capture \[\#phase-1-capture\]

\`\`\`python  
captured\_plan \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Fetch and analyze data"  
)  
\`\`\`

\*\*What Happens:\*\*

\* Prompt sent to ArmorIQ  
\* Plan generated (by LLM or template)  
\* Structure validated  
\* Plan stored with unique ID  
\* PlanCapture object returned

Phase 2: Canonicalization \[\#phase-2-canonicalization\]

\`\`\`python  
token \= client.get\_intent\_token(captured\_plan)  
\`\`\`

\*\*What Happens:\*\*

\* Plan converted to canonical form (CSRG)  
\* Deterministic hash generated  
\* Hash signs the token  
\* Token includes plan hash \+ policy \+ expiration

\*\*Canonical Form (CSRG):\*\*

\`\`\`json  
{  
  "nodes": \[  
    {"id": "n1", "action": "fetch\_data", "mcp": "data-mcp"},  
    {"id": "n2", "action": "analyze", "mcp": "analytics-mcp"}  
  \],  
  "edges": \[  
    {"from": "n1", "to": "n2"}  
  \]  
}  
\`\`\`

Phase 3: Verification \[\#phase-3-verification\]

\`\`\`python  
result \= client.invoke(  
    mcp="data-mcp",  
    action="fetch\_data",  
    intent\_token=token  
)  
\`\`\`

\*\*What Happens:\*\*

\* Proxy receives request  
\* Token signature verified  
\* Plan hash extracted  
\* Action checked against plan  
\* If match: request forwarded to MCP  
\* If mismatch: request rejected

Phase 4: Audit \[\#phase-4-audit\]

\*\*Automatically Logged:\*\*

\* Plan creation time  
\* Token generation time  
\* All action invocations  
\* Success/failure status  
\* Execution times

Plan Examples \[\#plan-examples\]

Example 1: Data Pipeline \[\#example-1-data-pipeline\]

\`\`\`python  
\# Natural language prompt  
captured \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Fetch customer data, validate it, and store in warehouse"  
)

\# Generated plan:  
{  
  "steps": \[  
    {"action": "fetch\_customers", "mcp": "data-mcp"},  
    {"action": "validate\_schema", "mcp": "validation-mcp"},  
    {"action": "store\_data", "mcp": "warehouse-mcp"}  
  \]  
}  
\`\`\`

Example 2: Financial Analysis \[\#example-2-financial-analysis\]

\`\`\`python  
\# Natural language prompt  
captured \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Analyze Q4 revenue, compare with forecast, generate report"  
)

\# Generated plan:  
{  
  "steps": \[  
    {"action": "fetch\_revenue", "mcp": "finance-mcp"},  
    {"action": "fetch\_forecast", "mcp": "finance-mcp"},  
    {"action": "compare\_metrics", "mcp": "analytics-mcp"},  
    {"action": "generate\_report", "mcp": "reporting-mcp"}  
  \]  
}  
\`\`\`

Example 3: Multi-Service Orchestration \[\#example-3-multi-service-orchestration\]

\`\`\`python  
\# Complex workflow  
captured \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Get user profile, check permissions, fetch data, apply transformations, send notification"  
)

\# Generated plan:  
{  
  "steps": \[  
    {"action": "get\_profile", "mcp": "auth-mcp"},  
    {"action": "check\_permissions", "mcp": "auth-mcp"},  
    {"action": "fetch\_data", "mcp": "data-mcp"},  
    {"action": "transform", "mcp": "etl-mcp"},  
    {"action": "send\_notification", "mcp": "notification-mcp"}  
  \]  
}  
\`\`\`

Best Practices \[\#best-practices\]

1\. Use Descriptive Prompts \[\#1-use-descriptive-prompts\]

\`\`\`python  
\# ✓ Good: Specific and clear  
prompt \= "Fetch sales data for 2024, calculate YoY growth, and generate PDF report"

\# ✗ Bad: Vague  
prompt \= "Do some data stuff"  
\`\`\`

2\. Include Context in Metadata \[\#2-include-context-in-metadata\]

\`\`\`python  
captured \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Process refund",  
    metadata={  
        "transaction\_id": "txn\_123",  
        "reason": "customer\_request",  
        "priority": "high"  
    }  
)  
\`\`\`

3\. Validate Plans Before Execution \[\#3-validate-plans-before-execution\]

\`\`\`python  
try:  
    captured \= client.capture\_plan(llm="gpt-4", prompt=user\_input)  
    print(f"Plan has {len(captured.plan\['steps'\])} steps")  
      
    \# Review plan before getting token  
    for step in captured.plan\['steps'\]:  
        print(f"- {step\['mcp'\]}/{step\['action'\]}")  
      
    \# Proceed if plan looks good  
    token \= client.get\_intent\_token(captured)  
except InvalidPlanError as e:  
    print(f"Plan validation failed: {e}")  
\`\`\`

4\. Use Plan Templates for Critical Workflows \[\#4-use-plan-templates-for-critical-workflows\]

\`\`\`python  
\# For regulatory compliance or safety-critical operations  
compliance\_template \= {  
    "steps": \[  
        {"action": "verify\_identity", "mcp": "kyc-mcp"},  
        {"action": "check\_sanctions", "mcp": "compliance-mcp"},  
        {"action": "approve\_transaction", "mcp": "approval-mcp"}  
    \]  
}

captured \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Execute compliance workflow",  
    plan=compliance\_template  
)  
\`\`\`

Common Issues \[\#common-issues\]

Issue: Plan Too Large \[\#issue-plan-too-large\]

\*\*Problem:\*\* Plan has \> 100 steps, causing timeouts

\*\*Solution:\*\* Break into multiple plans

\`\`\`python  
\# Split large workflows  
plan1 \= client.capture\_plan(llm="gpt-4", prompt="Fetch and validate data")  
plan2 \= client.capture\_plan(llm="gpt-4", prompt="Transform and load data")  
\`\`\`

Issue: Action Not in Registry \[\#issue-action-not-in-registry\]

\*\*Problem:\*\* MCP or action doesn't exist

\*\*Solution:\*\* Check available MCPs first

\`\`\`python  
\# Verify MCP exists  
available\_mcps \= client.list\_mcps()  
print(available\_mcps)  
\`\`\`

Issue: Plan Hash Mismatch \[\#issue-plan-hash-mismatch\]

\*\*Problem:\*\* Token verification fails

\*\*Solution:\*\* Don't modify captured plan after getting token

\`\`\`python  
\# ✓ Good  
captured \= client.capture\_plan(...)  
token \= client.get\_intent\_token(captured)  
client.invoke(..., intent\_token=token)

\# ✗ Bad: Modifying plan  
captured \= client.capture\_plan(...)  
captured.plan\['steps'\].append(...)  \# Don't do this\!  
token \= client.get\_intent\_token(captured)  \# Hash won't match  
\`\`\`

Next Steps \[\#next-steps\]

\* \[Token Lifecycle\](./token-lifecycle) \- How tokens work  
\* \[Security Model\](./security-model) \- Verification details  
\* \[Policy Management\](./policy-management) \- Control execution

\# Policy Management

Policy Management \[\#policy-management\]

Policies define \*\*what actions an agent can execute\*\*, providing fine-grained control over agent behavior. Think of policies as \*\*execution guardrails\*\* that work alongside intent verification.

What are Policies? \[\#what-are-policies\]

A policy is a set of rules that determines:

\* Which MCPs and actions are allowed/denied  
\* Time-based access restrictions  
\* Rate limits  
\* IP whitelisting  
\* Tool-level permissions

Policy Structure \[\#policy-structure\]

\`\`\`json  
{  
  "allow": \["analytics-mcp/\*", "data-mcp/fetch\_\*"\],  
  "deny": \["data-mcp/delete\_\*", "admin-mcp/\*"\],  
  "allowed\_tools": \["read\_file", "analyze", "aggregate"\],  
  "rate\_limit": 100,  
  "ip\_whitelist": \["10.0.0.0/8", "192.168.1.0/24"\],  
  "time\_restrictions": {  
    "allowed\_hours": \[9, 10, 11, 12, 13, 14, 15, 16, 17\],  
    "allowed\_days": \["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"\]  
  },  
  "priority": 50  
}  
\`\`\`

Policy Fields \[\#policy-fields\]

| Field               | Type       | Description                          | Example                    |  
| \------------------- | \---------- | \------------------------------------ | \-------------------------- |  
| \`allow\`             | list\\\[str\] | Allowed MCP/action patterns (glob)   | \`\["data-mcp/\*"\]\`           |  
| \`deny\`              | list\\\[str\] | Denied MCP/action patterns (glob)    | \`\["data-mcp/delete\_\*"\]\`    |  
| \`allowed\_tools\`     | list\\\[str\] | Whitelisted tool names               | \`\["read\_file", "analyze"\]\` |  
| \`rate\_limit\`        | int        | Max requests per hour                | \`100\`                      |  
| \`ip\_whitelist\`      | list\\\[str\] | Allowed IPs/CIDR ranges              | \`\["10.0.0.0/8"\]\`           |  
| \`time\_restrictions\` | object     | Time-based access control            | See below                  |  
| \`priority\`          | int        | Policy priority (0-100, higher wins) | \`50\`                       |

Time Restrictions \[\#time-restrictions\]

\`\`\`json  
{  
  "allowed\_hours": \[9, 10, 11, 12, 13, 14, 15, 16, 17\],  // 0-23  
  "allowed\_days": \["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"\]  
}  
\`\`\`

Creating Policies \[\#creating-policies\]

Method 1: Programmatic (SDK) \[\#method-1-programmatic-sdk\]

Define policies directly in your code:

\`\`\`python  
\# Restrictive policy for production agent  
policy \= {  
    "allow": \["analytics-mcp/\*", "data-mcp/fetch\_\*"\],  
    "deny": \["data-mcp/delete\_\*"\],  
    "allowed\_tools": \["read\_file", "analyze", "aggregate"\],  
    "rate\_limit": 100,  
    "ip\_whitelist": \["10.0.0.0/8"\],  
    "time\_restrictions": {  
        "allowed\_hours": \[9, 10, 11, 12, 13, 14, 15, 16, 17\],  
        "allowed\_days": \["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"\]  
    }  
}

token \= client.get\_intent\_token(  
    plan\_capture=plan,  
    policy=policy,  
    validity\_seconds=3600  
)  
\`\`\`

Method 2: Visual Policy Builder (ArmorIQ Canvas) \[\#method-2-visual-policy-builder-armoriq-canvas\]

Create policies using the drag-and-drop interface at \[platform.armoriq.ai/dashboard/policies\](https://platform.armoriq.ai/dashboard/policies):

\*\*Steps:\*\*

1\. Click "\*\*Canvas\*\*" button to open visual builder  
2\. Drag \*\*users\*\*, \*\*MCPs\*\*, and \*\*agents\*\* onto canvas  
3\. Connect entities with \*\*edges\*\* (connections)  
4\. Click edge to configure permissions visually  
5\. Use "\*\*Browse Tools\*\*" to select allowed tools from MCP  
6\. Set IP restrictions, time windows, rate limits  
7\. Save policy with name and priority

\*\*Use the policy ID in SDK:\*\*

\`\`\`python  
\# Use policy created in Canvas  
token \= client.get\_intent\_token(  
    plan\_capture=plan,  
    policy\_id="f88cf4c7-732d-44ff-901b-fd3d882c2ecf",  \# From Canvas  
    validity\_seconds=3600  
)  
\`\`\`

\*\*Or fetch policy JSON from API:\*\*

\`\`\`python  
import requests

\# Fetch policy from ArmorIQ API  
policy\_response \= requests.get(  
    f"https://customer-api.armoriq.ai/policies/f88cf4c7-732d-44ff-901b-fd3d882c2ecf",  
    headers={"Authorization": f"Bearer {user\_jwt}"}  
)  
policy \= policy\_response.json()\["data"\]\["permissions"\]

\# Use fetched policy  
token \= client.get\_intent\_token(  
    plan\_capture=plan,  
    policy=policy,  
    validity\_seconds=3600  
)  
\`\`\`

Policy Evaluation \[\#policy-evaluation\]

How Policies are Applied \[\#how-policies-are-applied\]

When you request an intent token, ArmorIQ:

1\. \*\*Loads\*\* applicable policies (user, agent, organization level)  
2\. \*\*Merges\*\* policies by priority (higher priority wins)  
3\. \*\*Evaluates\*\* plan actions against merged policy  
4\. \*\*Rejects\*\* token if any action violates policy  
5\. \*\*Embeds\*\* policy hash in token

At invocation time, ArmorIQ:

1\. \*\*Extracts\*\* policy from token  
2\. \*\*Checks\*\* if action matches allow/deny patterns  
3\. \*\*Verifies\*\* time restrictions (if any)  
4\. \*\*Checks\*\* rate limits  
5\. \*\*Validates\*\* IP address (if whitelist exists)  
6\. \*\*Allows\*\* or \*\*denies\*\* request

Allow/Deny Pattern Matching \[\#allowdeny-pattern-matching\]

Policies use \*\*glob patterns\*\* for flexible matching:

\`\`\`python  
policy \= {  
    "allow": \[  
        "data-mcp/\*",           \# All data-mcp actions  
        "analytics-mcp/fetch\_\*" \# Only fetch actions in analytics-mcp  
    \],  
    "deny": \[  
        "data-mcp/delete\_\*",    \# No delete actions  
        "admin-mcp/\*"           \# No admin actions at all  
    \]  
}  
\`\`\`

\*\*Matching Rules:\*\*

\* \`\*\` matches any string  
\* \`data-mcp/\*\` matches \`data-mcp/fetch\`, \`data-mcp/analyze\`, etc.  
\* \`data-mcp/fetch\_\*\` matches \`data-mcp/fetch\_users\`, \`data-mcp/fetch\_orders\`, etc.  
\* Deny takes precedence over allow

Priority Resolution \[\#priority-resolution\]

When multiple policies apply:

\`\`\`python  
\# User-level policy (priority 30\)  
user\_policy \= {  
    "allow": \["data-mcp/\*"\],  
    "priority": 30  
}

\# Agent-level policy (priority 60\)  
agent\_policy \= {  
    "deny": \["data-mcp/delete\_\*"\],  
    "priority": 60  
}

\# Organization-level policy (priority 90\)  
org\_policy \= {  
    "allow": \["analytics-mcp/\*"\],  
    "priority": 90  
}

\# Merged result:  
\# \- data-mcp/\* allowed (user policy)  
\# \- data-mcp/delete\_\* denied (agent policy, higher priority)  
\# \- analytics-mcp/\* allowed (org policy, highest priority)  
\`\`\`

Policy Examples \[\#policy-examples\]

Example 1: Read-Only Agent \[\#example-1-read-only-agent\]

\`\`\`python  
\# Agent can only read data, no writes  
readonly\_policy \= {  
    "allow": \[  
        "data-mcp/fetch\_\*",  
        "data-mcp/query\_\*",  
        "analytics-mcp/analyze\_\*"  
    \],  
    "deny": \[  
        "data-mcp/insert\_\*",  
        "data-mcp/update\_\*",  
        "data-mcp/delete\_\*"  
    \],  
    "rate\_limit": 1000  
}  
\`\`\`

Example 2: Business Hours Only \[\#example-2-business-hours-only\]

\`\`\`python  
\# Agent only works during business hours  
business\_hours\_policy \= {  
    "allow": \["\*"\],  
    "time\_restrictions": {  
        "allowed\_hours": \[9, 10, 11, 12, 13, 14, 15, 16, 17\],  
        "allowed\_days": \["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"\]  
    }  
}  
\`\`\`

Example 3: High-Security Agent \[\#example-3-high-security-agent\]

\`\`\`python  
\# Agent with strict security constraints  
secure\_policy \= {  
    "allow": \["finance-mcp/fetch\_balance", "finance-mcp/calculate\_\*"\],  
    "deny": \["finance-mcp/transfer\_\*", "finance-mcp/withdraw\_\*"\],  
    "ip\_whitelist": \["10.0.0.0/8"\],  \# Internal network only  
    "rate\_limit": 50,  
    "time\_restrictions": {  
        "allowed\_hours": \[9, 10, 11, 12, 13, 14, 15, 16, 17\],  
        "allowed\_days": \["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"\]  
    }  
}  
\`\`\`

Example 4: Development Agent \[\#example-4-development-agent\]

\`\`\`python  
\# Permissive policy for development  
dev\_policy \= {  
    "allow": \["\*"\],  
    "deny": \["production-mcp/\*"\],  \# No production access  
    "rate\_limit": 10000  
}  
\`\`\`

Policy Composition \[\#policy-composition\]

You can compose policies for different scenarios:

\`\`\`python  
def get\_policy(environment: str, role: str) \-\> dict:  
    """Get policy based on environment and role."""  
      
    base\_policy \= {  
        "rate\_limit": 100,  
        "priority": 50  
    }  
      
    \# Environment-specific  
    if environment \== "production":  
        base\_policy\["ip\_whitelist"\] \= \["10.0.0.0/8"\]  
        base\_policy\["time\_restrictions"\] \= {  
            "allowed\_hours": list(range(9, 18)),  
            "allowed\_days": \["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"\]  
        }  
      
    \# Role-specific  
    if role \== "admin":  
        base\_policy\["allow"\] \= \["\*"\]  
        base\_policy\["rate\_limit"\] \= 1000  
    elif role \== "analyst":  
        base\_policy\["allow"\] \= \["data-mcp/fetch\_\*", "analytics-mcp/\*"\]  
        base\_policy\["deny"\] \= \["data-mcp/delete\_\*"\]  
    elif role \== "viewer":  
        base\_policy\["allow"\] \= \["data-mcp/fetch\_\*"\]  
        base\_policy\["deny"\] \= \["\*"\]  
      
    return base\_policy

\# Usage  
policy \= get\_policy(environment="production", role="analyst")  
token \= client.get\_intent\_token(plan\_capture=plan, policy=policy)  
\`\`\`

Testing Policies \[\#testing-policies\]

1\. Dry Run Validation \[\#1-dry-run-validation\]

\`\`\`python  
\# Validate policy without executing  
try:  
    token \= client.get\_intent\_token(  
        plan\_capture=plan,  
        policy=test\_policy,  
        dry\_run=True  \# Don't create token, just validate  
    )  
    print("✓ Policy is valid")  
except PolicyViolationError as e:  
    print(f"✗ Policy violation: {e}")  
\`\`\`

2\. Policy Simulation \[\#2-policy-simulation\]

\`\`\`python  
\# Test if action would be allowed  
def simulate\_policy(policy: dict, mcp: str, action: str) \-\> bool:  
    """Check if action would be allowed by policy."""  
    full\_action \= f"{mcp}/{action}"  
      
    \# Check deny patterns  
    for pattern in policy.get("deny", \[\]):  
        if fnmatch.fnmatch(full\_action, pattern):  
            return False  
      
    \# Check allow patterns  
    for pattern in policy.get("allow", \[\]):  
        if fnmatch.fnmatch(full\_action, pattern):  
            return True  
      
    return False

\# Usage  
policy \= {"allow": \["data-mcp/\*"\], "deny": \["data-mcp/delete\_\*"\]}  
print(simulate\_policy(policy, "data-mcp", "fetch\_data"))  \# True  
print(simulate\_policy(policy, "data-mcp", "delete\_all"))  \# False  
\`\`\`

Policy Management Best Practices \[\#policy-management-best-practices\]

1\. Start Restrictive, Then Relax \[\#1-start-restrictive-then-relax\]

\`\`\`python  
\# Start with minimal permissions  
initial\_policy \= {  
    "allow": \["data-mcp/fetch\_data"\],  
    "deny": \["\*"\]  
}

\# Add permissions as needed  
expanded\_policy \= {  
    "allow": \["data-mcp/fetch\_\*", "analytics-mcp/analyze"\],  
    "deny": \["data-mcp/delete\_\*"\]  
}  
\`\`\`

2\. Use Environment-Specific Policies \[\#2-use-environment-specific-policies\]

\`\`\`python  
policies \= {  
    "development": {  
        "allow": \["\*"\],  
        "deny": \["production-mcp/\*"\],  
        "rate\_limit": 10000  
    },  
    "staging": {  
        "allow": \["\*"\],  
        "deny": \["production-mcp/\*"\],  
        "rate\_limit": 1000  
    },  
    "production": {  
        "allow": \["data-mcp/fetch\_\*", "analytics-mcp/\*"\],  
        "deny": \["data-mcp/delete\_\*"\],  
        "rate\_limit": 100,  
        "ip\_whitelist": \["10.0.0.0/8"\]  
    }  
}

env \= os.getenv("ENVIRONMENT", "development")  
policy \= policies\[env\]  
\`\`\`

3\. Version Your Policies \[\#3-version-your-policies\]

\`\`\`python  
policy\_v1 \= {  
    "version": "1.0.0",  
    "allow": \["data-mcp/\*"\],  
    "deny": \[\]  
}

policy\_v2 \= {  
    "version": "2.0.0",  
    "allow": \["data-mcp/\*", "analytics-mcp/\*"\],  
    "deny": \["data-mcp/delete\_\*"\]  
}

\# Use version in metadata  
token \= client.get\_intent\_token(  
    plan\_capture=plan,  
    policy=policy\_v2,  
    metadata={"policy\_version": "2.0.0"}  
)  
\`\`\`

4\. Monitor Policy Violations \[\#4-monitor-policy-violations\]

\`\`\`python  
\# Log policy violations for security monitoring  
try:  
    token \= client.get\_intent\_token(plan\_capture=plan, policy=policy)  
except PolicyViolationError as e:  
    logger.error(f"Policy violation: {e}", extra={  
        "user\_id": user\_id,  
        "agent\_id": agent\_id,  
        "violated\_action": e.action,  
        "policy": policy  
    })  
    raise  
\`\`\`

Common Policy Patterns \[\#common-policy-patterns\]

Pattern 1: Separation of Concerns \[\#pattern-1-separation-of-concerns\]

\`\`\`python  
\# Data team: Read-only access to data  
data\_team\_policy \= {  
    "allow": \["data-mcp/fetch\_\*", "data-mcp/query\_\*"\],  
    "deny": \["data-mcp/insert\_\*", "data-mcp/delete\_\*"\]  
}

\# Analytics team: Read \+ compute  
analytics\_team\_policy \= {  
    "allow": \["data-mcp/fetch\_\*", "analytics-mcp/\*"\],  
    "deny": \["data-mcp/insert\_\*", "data-mcp/delete\_\*"\]  
}

\# Admin team: Full access  
admin\_team\_policy \= {  
    "allow": \["\*"\],  
    "deny": \[\]  
}  
\`\`\`

Pattern 2: Progressive Permissions \[\#pattern-2-progressive-permissions\]

\`\`\`python  
\# Level 1: Basic access  
level1\_policy \= {  
    "allow": \["data-mcp/fetch\_public\_\*"\],  
    "rate\_limit": 100  
}

\# Level 2: Intermediate access  
level2\_policy \= {  
    "allow": \["data-mcp/fetch\_\*", "analytics-mcp/basic\_\*"\],  
    "rate\_limit": 500  
}

\# Level 3: Advanced access  
level3\_policy \= {  
    "allow": \["data-mcp/\*", "analytics-mcp/\*"\],  
    "deny": \["data-mcp/delete\_\*"\],  
    "rate\_limit": 1000  
}  
\`\`\`

Next Steps \[\#next-steps\]

\* \[get\\\_intent\\\_token()\](../core-methods/get-intent-token) \- Apply policies to tokens  
\* \[Security Model\](./security-model) \- Understand verification  
\* \[Token Lifecycle\](./token-lifecycle) \- How tokens work

\# Token Lifecycle

Token Lifecycle \[\#token-lifecycle\]

Intent tokens are \*\*cryptographically signed credentials\*\* that authorize execution of specific actions. Understanding their lifecycle is crucial for secure agent operation.

Token Phases \[\#token-phases\]

Phase 1: Plan Capture \[\#phase-1-plan-capture\]

\`\`\`python  
captured \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Fetch and analyze data"  
)  
\`\`\`

\*\*What Happens:\*\*

\* Plan structure created  
\* Plan validated against MCP registry  
\* Plan stored with unique ID  
\* Canonical representation (CSRG) generated

Phase 2: Token Generation \[\#phase-2-token-generation\]

\`\`\`python  
token \= client.get\_intent\_token(  
    plan\_capture=captured,  
    policy={"allow": \["\*"\], "deny": \[\]},  
    validity\_seconds=3600  
)  
\`\`\`

\*\*What Happens:\*\*

1\. Plan canonicalized to CSRG format  
2\. Plan hash computed (SHA-256 of canonical form)  
3\. Policy applied and validated  
4\. JWT token created with:  
   \* Plan hash  
   \* Policy hash  
   \* User/agent identity  
   \* Expiration time  
   \* Signature  
5\. Token signed by CSRG-IAP using Ed25519  
6\. Token returned to agent

Phase 3: Token Usage \[\#phase-3-token-usage\]

\`\`\`python  
result \= client.invoke(  
    mcp="data-mcp",  
    action="fetch\_data",  
    intent\_token=token,  
    params={...}  
)  
\`\`\`

\*\*What Happens:\*\*

1\. Token sent to ArmorIQ Proxy  
2\. Token signature verified  
3\. Token expiration checked  
4\. Plan hash extracted and verified  
5\. Action checked against plan  
6\. Policy constraints validated  
7\. If all checks pass: action forwarded to MCP  
8\. If any check fails: request rejected

Phase 4: Token Expiration \[\#phase-4-token-expiration\]

Tokens expire based on \`validity\_seconds\` parameter. After expiration:

\* Token becomes invalid  
\* All invocations using token will fail  
\* New token must be requested

Token Structure (JWT) \[\#token-structure-jwt\]

Header \[\#header\]

\`\`\`json  
{  
  "alg": "EdDSA",  
  "typ": "JWT"  
}  
\`\`\`

Payload \[\#payload\]

\`\`\`json  
{  
  "plan\_hash": "sha256:abc123...",  
  "policy\_hash": "sha256:def456...",  
  "user\_id": "user\_123",  
  "agent\_id": "agent\_xyz",  
  "org\_id": "org\_001",  
  "iat": 1234567800,  
  "exp": 1234571400,  
  "iss": "armoriq-csrg-iap",  
  "jti": "token\_unique\_id"  
}  
\`\`\`

Signature \[\#signature\]

\`\`\`  
EdDSA signature using CSRG-IAP's private key  
\`\`\`

Token Properties \[\#token-properties\]

Immutability \[\#immutability\]

Once generated, tokens cannot be modified. Any change invalidates the signature.

\`\`\`python  
\# ✗ Bad: Don't try to modify token  
token.token \= token.token \+ "extra"  \# Signature will fail

\# ✓ Good: Generate new token if needed  
new\_token \= client.get\_intent\_token(captured, validity\_seconds=7200)  
\`\`\`

Non-Transferability \[\#non-transferability\]

Tokens are bound to specific user/agent IDs and cannot be used by others.

\`\`\`python  
\# Token bound to this user/agent  
token \= client.get\_intent\_token(captured)

\# Another agent cannot use this token  
other\_client \= ArmorIQClient(user\_id="other\_user", agent\_id="other\_agent")  
other\_client.invoke(..., intent\_token=token)  \# ✗ Fails: user/agent mismatch  
\`\`\`

Time-Limited \[\#time-limited\]

Tokens have explicit expiration times for security.

\`\`\`python  
\# Short-lived token (60 seconds)  
token\_short \= client.get\_intent\_token(captured, validity\_seconds=60)

\# Long-lived token (1 hour)  
token\_long \= client.get\_intent\_token(captured, validity\_seconds=3600)

\# Check expiration  
print(f"Expires at: {token\_short.expires\_at}")  
\`\`\`

Token Management Best Practices \[\#token-management-best-practices\]

1\. Use Appropriate Validity Periods \[\#1-use-appropriate-validity-periods\]

\`\`\`python  
\# ✓ Good: Match validity to use case  
token\_quick \= client.get\_intent\_token(captured, validity\_seconds=300)   \# 5 min for quick tasks  
token\_batch \= client.get\_intent\_token(captured, validity\_seconds=3600)  \# 1 hour for batch jobs  
token\_interactive \= client.get\_intent\_token(captured, validity\_seconds=1800)  \# 30 min for user sessions

\# ✗ Bad: Overly long validity  
token\_long \= client.get\_intent\_token(captured, validity\_seconds=86400)  \# 24 hours \- too long\!  
\`\`\`

2\. Handle Token Expiration Gracefully \[\#2-handle-token-expiration-gracefully\]

\`\`\`python  
from armoriq\_sdk.exceptions import TokenExpiredError

def invoke\_with\_refresh(client, mcp, action, token, captured, params):  
    """Invoke with automatic token refresh on expiration."""  
    try:  
        return client.invoke(mcp, action, token, params)  
    except TokenExpiredError:  
        \# Token expired, get new one  
        new\_token \= client.get\_intent\_token(captured)  
        return client.invoke(mcp, action, new\_token, params)  
\`\`\`

3\. Cache Tokens for Repeated Use \[\#3-cache-tokens-for-repeated-use\]

\`\`\`python  
class TokenManager:  
    def \_\_init\_\_(self, client):  
        self.client \= client  
        self.token \= None  
        self.captured \= None  
      
    def ensure\_token(self, prompt, validity\_seconds=3600):  
        """Get or refresh token as needed."""  
        if self.token and self.token.expires\_at \> time.time() \+ 60:  
            return self.token  
          
        \# Need new token  
        self.captured \= self.client.capture\_plan(llm="gpt-4", prompt=prompt)  
        self.token \= self.client.get\_intent\_token(  
            self.captured,  
            validity\_seconds=validity\_seconds  
        )  
        return self.token

\# Usage  
manager \= TokenManager(client)  
token \= manager.ensure\_token("Fetch and analyze data")  
result \= client.invoke("data-mcp", "fetch\_data", token, {...})  
\`\`\`

4\. Revoke Tokens When Done \[\#4-revoke-tokens-when-done\]

\`\`\`python  
\# Not directly supported yet, but use short validity as mitigation  
token \= client.get\_intent\_token(captured, validity\_seconds=300)  \# 5 min only

\# For long-running tasks, periodically refresh  
for i in range(100):  
    if i % 10 \== 0:  
        \# Refresh token every 10 iterations  
        token \= client.get\_intent\_token(captured, validity\_seconds=300)  
      
    result \= client.invoke("data-mcp", "process", token, {"batch": i})  
\`\`\`

Token Verification Process \[\#token-verification-process\]

When you invoke an action, the proxy verifies:

Step 1: Signature Verification \[\#step-1-signature-verification\]

\`\`\`  
1\. Extract JWT header, payload, signature  
2\. Reconstruct signing input: base64(header) \+ "." \+ base64(payload)  
3\. Verify signature using CSRG-IAP public key  
4\. If signature invalid → REJECT  
\`\`\`

Step 2: Expiration Check \[\#step-2-expiration-check\]

\`\`\`  
1\. Extract "exp" from payload  
2\. Check if current\_time \< exp  
3\. If expired → REJECT  
\`\`\`

Step 3: Identity Verification \[\#step-3-identity-verification\]

\`\`\`  
1\. Extract user\_id, agent\_id from payload  
2\. Compare with request's user\_id, agent\_id  
3\. If mismatch → REJECT  
\`\`\`

Step 4: Plan Verification \[\#step-4-plan-verification\]

\`\`\`  
1\. Extract plan\_hash from payload  
2\. Check if requested action is in plan  
3\. If action not in plan → REJECT  
\`\`\`

Step 5: Policy Verification \[\#step-5-policy-verification\]

\`\`\`  
1\. Extract policy\_hash from payload  
2\. Apply policy rules to requested action  
3\. If action violates policy → REJECT  
\`\`\`

Step 6: Rate Limit Check \[\#step-6-rate-limit-check\]

\`\`\`  
1\. Check invocation count for this user/agent  
2\. If rate limit exceeded → REJECT  
\`\`\`

\*\*If all checks pass → ALLOW and forward to MCP\*\*

Token Security Properties \[\#token-security-properties\]

Cryptographic Binding \[\#cryptographic-binding\]

Tokens are cryptographically bound to:

\* \*\*Plan\*\*: Cannot execute actions outside plan  
\* \*\*User/Agent\*\*: Cannot be used by different identity  
\* \*\*Policy\*\*: Cannot bypass policy constraints  
\* \*\*Time\*\*: Cannot be used after expiration

Non-Repudiation \[\#non-repudiation\]

Every invocation creates an audit log with:

\* Token ID  
\* User/Agent ID  
\* Action executed  
\* Timestamp  
\* Result

This provides complete auditability.

Defense in Depth \[\#defense-in-depth\]

Even if an attacker obtains a token:

\* Cannot modify it (signature verification)  
\* Cannot reuse it as different user (identity binding)  
\* Cannot execute unplanned actions (plan hash verification)  
\* Cannot use after expiration (time-limited)

Common Token Issues \[\#common-token-issues\]

Issue: Token Expired \[\#issue-token-expired\]

\*\*Symptom:\*\* \`TokenExpiredError\` when invoking

\*\*Solution:\*\*

\`\`\`python  
\# Refresh token  
new\_token \= client.get\_intent\_token(captured, validity\_seconds=3600)  
result \= client.invoke(mcp, action, new\_token, params)  
\`\`\`

Issue: Action Not in Plan \[\#issue-action-not-in-plan\]

\*\*Symptom:\*\* \`IntentVerificationError: Action not in plan\`

\*\*Solution:\*\*

\`\`\`python  
\# Capture new plan that includes the action  
captured \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Fetch data and also do analysis"  \# Include both actions  
)  
token \= client.get\_intent\_token(captured)  
\`\`\`

Issue: Token Signature Invalid \[\#issue-token-signature-invalid\]

\*\*Symptom:\*\* \`InvalidTokenError: Signature verification failed\`

\*\*Solution:\*\*

\* Don't modify token after generation  
\* Ensure token was generated by legitimate CSRG-IAP  
\* Check network isn't corrupting token

Issue: Identity Mismatch \[\#issue-identity-mismatch\]

\*\*Symptom:\*\* \`AuthenticationError: Token user\_id/agent\_id mismatch\`

\*\*Solution:\*\*

\`\`\`python  
\# Use same client that generated token  
\# ✓ Good  
token \= client.get\_intent\_token(captured)  
result \= client.invoke(mcp, action, token, params)

\# ✗ Bad: Different client  
other\_client \= ArmorIQClient(user\_id="different\_user", ...)  
result \= other\_client.invoke(mcp, action, token, params)  \# Fails  
\`\`\`

Next Steps \[\#next-steps\]

\* \[Security Model\](./security-model) \- Deep dive into security  
\* \[Core Methods\](../core-methods) \- Using tokens in practice  
\* \[Error Handling\](../error-handling) \- Handle token errors

\# Token Lifecycle

Token Lifecycle \[\#token-lifecycle\]

Intent tokens are \*\*cryptographically signed credentials\*\* that authorize execution of specific actions. Understanding their lifecycle is crucial for secure agent operation.

Token Phases \[\#token-phases\]

Phase 1: Plan Capture \[\#phase-1-plan-capture\]

\`\`\`python  
captured \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Fetch and analyze data"  
)  
\`\`\`

\*\*What Happens:\*\*

\* Plan structure created  
\* Plan validated against MCP registry  
\* Plan stored with unique ID  
\* Canonical representation (CSRG) generated

Phase 2: Token Generation \[\#phase-2-token-generation\]

\`\`\`python  
token \= client.get\_intent\_token(  
    plan\_capture=captured,  
    policy={"allow": \["\*"\], "deny": \[\]},  
    validity\_seconds=3600  
)  
\`\`\`

\*\*What Happens:\*\*

1\. Plan canonicalized to CSRG format  
2\. Plan hash computed (SHA-256 of canonical form)  
3\. Policy applied and validated  
4\. JWT token created with:  
   \* Plan hash  
   \* Policy hash  
   \* User/agent identity  
   \* Expiration time  
   \* Signature  
5\. Token signed by CSRG-IAP using Ed25519  
6\. Token returned to agent

Phase 3: Token Usage \[\#phase-3-token-usage\]

\`\`\`python  
result \= client.invoke(  
    mcp="data-mcp",  
    action="fetch\_data",  
    intent\_token=token,  
    params={...}  
)  
\`\`\`

\*\*What Happens:\*\*

1\. Token sent to ArmorIQ Proxy  
2\. Token signature verified  
3\. Token expiration checked  
4\. Plan hash extracted and verified  
5\. Action checked against plan  
6\. Policy constraints validated  
7\. If all checks pass: action forwarded to MCP  
8\. If any check fails: request rejected

Phase 4: Token Expiration \[\#phase-4-token-expiration\]

Tokens expire based on \`validity\_seconds\` parameter. After expiration:

\* Token becomes invalid  
\* All invocations using token will fail  
\* New token must be requested

Token Structure (JWT) \[\#token-structure-jwt\]

Header \[\#header\]

\`\`\`json  
{  
  "alg": "EdDSA",  
  "typ": "JWT"  
}  
\`\`\`

Payload \[\#payload\]

\`\`\`json  
{  
  "plan\_hash": "sha256:abc123...",  
  "policy\_hash": "sha256:def456...",  
  "user\_id": "user\_123",  
  "agent\_id": "agent\_xyz",  
  "org\_id": "org\_001",  
  "iat": 1234567800,  
  "exp": 1234571400,  
  "iss": "armoriq-csrg-iap",  
  "jti": "token\_unique\_id"  
}  
\`\`\`

Signature \[\#signature\]

\`\`\`  
EdDSA signature using CSRG-IAP's private key  
\`\`\`

Token Properties \[\#token-properties\]

Immutability \[\#immutability\]

Once generated, tokens cannot be modified. Any change invalidates the signature.

\`\`\`python  
\# ✗ Bad: Don't try to modify token  
token.token \= token.token \+ "extra"  \# Signature will fail

\# ✓ Good: Generate new token if needed  
new\_token \= client.get\_intent\_token(captured, validity\_seconds=7200)  
\`\`\`

Non-Transferability \[\#non-transferability\]

Tokens are bound to specific user/agent IDs and cannot be used by others.

\`\`\`python  
\# Token bound to this user/agent  
token \= client.get\_intent\_token(captured)

\# Another agent cannot use this token  
other\_client \= ArmorIQClient(user\_id="other\_user", agent\_id="other\_agent")  
other\_client.invoke(..., intent\_token=token)  \# ✗ Fails: user/agent mismatch  
\`\`\`

Time-Limited \[\#time-limited\]

Tokens have explicit expiration times for security.

\`\`\`python  
\# Short-lived token (60 seconds)  
token\_short \= client.get\_intent\_token(captured, validity\_seconds=60)

\# Long-lived token (1 hour)  
token\_long \= client.get\_intent\_token(captured, validity\_seconds=3600)

\# Check expiration  
print(f"Expires at: {token\_short.expires\_at}")  
\`\`\`

Token Management Best Practices \[\#token-management-best-practices\]

1\. Use Appropriate Validity Periods \[\#1-use-appropriate-validity-periods\]

\`\`\`python  
\# ✓ Good: Match validity to use case  
token\_quick \= client.get\_intent\_token(captured, validity\_seconds=300)   \# 5 min for quick tasks  
token\_batch \= client.get\_intent\_token(captured, validity\_seconds=3600)  \# 1 hour for batch jobs  
token\_interactive \= client.get\_intent\_token(captured, validity\_seconds=1800)  \# 30 min for user sessions

\# ✗ Bad: Overly long validity  
token\_long \= client.get\_intent\_token(captured, validity\_seconds=86400)  \# 24 hours \- too long\!  
\`\`\`

2\. Handle Token Expiration Gracefully \[\#2-handle-token-expiration-gracefully\]

\`\`\`python  
from armoriq\_sdk.exceptions import TokenExpiredError

def invoke\_with\_refresh(client, mcp, action, token, captured, params):  
    """Invoke with automatic token refresh on expiration."""  
    try:  
        return client.invoke(mcp, action, token, params)  
    except TokenExpiredError:  
        \# Token expired, get new one  
        new\_token \= client.get\_intent\_token(captured)  
        return client.invoke(mcp, action, new\_token, params)  
\`\`\`

3\. Cache Tokens for Repeated Use \[\#3-cache-tokens-for-repeated-use\]

\`\`\`python  
class TokenManager:  
    def \_\_init\_\_(self, client):  
        self.client \= client  
        self.token \= None  
        self.captured \= None  
      
    def ensure\_token(self, prompt, validity\_seconds=3600):  
        """Get or refresh token as needed."""  
        if self.token and self.token.expires\_at \> time.time() \+ 60:  
            return self.token  
          
        \# Need new token  
        self.captured \= self.client.capture\_plan(llm="gpt-4", prompt=prompt)  
        self.token \= self.client.get\_intent\_token(  
            self.captured,  
            validity\_seconds=validity\_seconds  
        )  
        return self.token

\# Usage  
manager \= TokenManager(client)  
token \= manager.ensure\_token("Fetch and analyze data")  
result \= client.invoke("data-mcp", "fetch\_data", token, {...})  
\`\`\`

4\. Revoke Tokens When Done \[\#4-revoke-tokens-when-done\]

\`\`\`python  
\# Not directly supported yet, but use short validity as mitigation  
token \= client.get\_intent\_token(captured, validity\_seconds=300)  \# 5 min only

\# For long-running tasks, periodically refresh  
for i in range(100):  
    if i % 10 \== 0:  
        \# Refresh token every 10 iterations  
        token \= client.get\_intent\_token(captured, validity\_seconds=300)  
      
    result \= client.invoke("data-mcp", "process", token, {"batch": i})  
\`\`\`

Token Verification Process \[\#token-verification-process\]

When you invoke an action, the proxy verifies:

Step 1: Signature Verification \[\#step-1-signature-verification\]

\`\`\`  
1\. Extract JWT header, payload, signature  
2\. Reconstruct signing input: base64(header) \+ "." \+ base64(payload)  
3\. Verify signature using CSRG-IAP public key  
4\. If signature invalid → REJECT  
\`\`\`

Step 2: Expiration Check \[\#step-2-expiration-check\]

\`\`\`  
1\. Extract "exp" from payload  
2\. Check if current\_time \< exp  
3\. If expired → REJECT  
\`\`\`

Step 3: Identity Verification \[\#step-3-identity-verification\]

\`\`\`  
1\. Extract user\_id, agent\_id from payload  
2\. Compare with request's user\_id, agent\_id  
3\. If mismatch → REJECT  
\`\`\`

Step 4: Plan Verification \[\#step-4-plan-verification\]

\`\`\`  
1\. Extract plan\_hash from payload  
2\. Check if requested action is in plan  
3\. If action not in plan → REJECT  
\`\`\`

Step 5: Policy Verification \[\#step-5-policy-verification\]

\`\`\`  
1\. Extract policy\_hash from payload  
2\. Apply policy rules to requested action  
3\. If action violates policy → REJECT  
\`\`\`

Step 6: Rate Limit Check \[\#step-6-rate-limit-check\]

\`\`\`  
1\. Check invocation count for this user/agent  
2\. If rate limit exceeded → REJECT  
\`\`\`

\*\*If all checks pass → ALLOW and forward to MCP\*\*

Token Security Properties \[\#token-security-properties\]

Cryptographic Binding \[\#cryptographic-binding\]

Tokens are cryptographically bound to:

\* \*\*Plan\*\*: Cannot execute actions outside plan  
\* \*\*User/Agent\*\*: Cannot be used by different identity  
\* \*\*Policy\*\*: Cannot bypass policy constraints  
\* \*\*Time\*\*: Cannot be used after expiration

Non-Repudiation \[\#non-repudiation\]

Every invocation creates an audit log with:

\* Token ID  
\* User/Agent ID  
\* Action executed  
\* Timestamp  
\* Result

This provides complete auditability.

Defense in Depth \[\#defense-in-depth\]

Even if an attacker obtains a token:

\* Cannot modify it (signature verification)  
\* Cannot reuse it as different user (identity binding)  
\* Cannot execute unplanned actions (plan hash verification)  
\* Cannot use after expiration (time-limited)

Common Token Issues \[\#common-token-issues\]

Issue: Token Expired \[\#issue-token-expired\]

\*\*Symptom:\*\* \`TokenExpiredError\` when invoking

\*\*Solution:\*\*

\`\`\`python  
\# Refresh token  
new\_token \= client.get\_intent\_token(captured, validity\_seconds=3600)  
result \= client.invoke(mcp, action, new\_token, params)  
\`\`\`

Issue: Action Not in Plan \[\#issue-action-not-in-plan\]

\*\*Symptom:\*\* \`IntentVerificationError: Action not in plan\`

\*\*Solution:\*\*

\`\`\`python  
\# Capture new plan that includes the action  
captured \= client.capture\_plan(  
    llm="gpt-4",  
    prompt="Fetch data and also do analysis"  \# Include both actions  
)  
token \= client.get\_intent\_token(captured)  
\`\`\`

Issue: Token Signature Invalid \[\#issue-token-signature-invalid\]

\*\*Symptom:\*\* \`InvalidTokenError: Signature verification failed\`

\*\*Solution:\*\*

\* Don't modify token after generation  
\* Ensure token was generated by legitimate CSRG-IAP  
\* Check network isn't corrupting token

Issue: Identity Mismatch \[\#issue-identity-mismatch\]

\*\*Symptom:\*\* \`AuthenticationError: Token user\_id/agent\_id mismatch\`

\*\*Solution:\*\*

\`\`\`python  
\# Use same client that generated token  
\# ✓ Good  
token \= client.get\_intent\_token(captured)  
result \= client.invoke(mcp, action, token, params)

\# ✗ Bad: Different client  
other\_client \= ArmorIQClient(user\_id="different\_user", ...)  
result \= other\_client.invoke(mcp, action, token, params)  \# Fails  
\`\`\`

Next Steps \[\#next-steps\]

\* \[Security Model\](./security-model) \- Deep dive into security  
\* \[Core Methods\](../core-methods) \- Using tokens in practice  
\* \[Error Handling\](../error-handling) \- Handle token errors

\# Core Methods

Core Methods \[\#core-methods\]

Each core method has its own page. Use the sections below to jump directly to the method you need.

Methods \[\#methods\]

\* \[capture\\\_plan()\](/docs/core-methods/capture-plan)  
\* \[get\\\_intent\\\_token()\](/docs/core-methods/get-intent-token)  
\* \[invoke()\](/docs/core-methods/invoke)  
\* \[delegate()\](/docs/core-methods/delegate)

\# capture\_plan()

\*\*Design Philosophy\*\*: It captures the agent's intent by accepting an explicit plan structure. You define which MCPs and actions the agent will execute. The SDK validates the plan structure, then CSRG-IAP creates the cryptographic proof. This is the foundation of ArmorIQ's intent-based security model.

Captures and validates an execution plan structure. The plan must explicitly define the steps the agent intends to execute based on your onboarded MCPs.

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    client.capture\_plan(  
        llm: str,  
        prompt: str,  
        plan: dict,              \# REQUIRED  
        metadata: dict \= None  
    ) \-\> PlanCapture  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    client.capturePlan(  
      llm: string,  
      prompt: string,  
      plan: Record\<string, any\>,  // REQUIRED  
      metadata?: Record\<string, any\>  
    ): PlanCapture  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Required Plan Structure \[\#required-plan-structure\]

You must provide an explicit plan with your onboarded MCPs and their tools:

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# Define your execution plan  
    plan \= {  
        "goal": "Search for Coldplay concerts",  \# Required: what you want to accomplish  
        "steps": \[                                \# Required: array of actions  
            {  
                "action": "search\_events",        \# Tool name from your MCP  
                "mcp": "ticketmaster-mcp",       \# Your onboarded MCP identifier  
                "params": {"artist": "Coldplay"}  \# Tool parameters  
            }  
        \]  
    }

    \# Capture the plan (SDK validates structure)  
    captured \= client.capture\_plan(  
        llm="gpt-4",  
        prompt="Find Coldplay concerts",  
        plan=plan  \# REQUIRED  
    )  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    // Define your execution plan  
    const plan \= {  
      goal: 'Search for Coldplay concerts',   // Required: what you want to accomplish  
      steps: \[                                 // Required: array of actions  
        {  
          action: 'search\_events',            // Tool name from your MCP  
          mcp: 'ticketmaster-mcp',           // Your onboarded MCP identifier  
          params: { artist: 'Coldplay' }      // Tool parameters  
        }  
      \]  
    };

    // Capture the plan (SDK validates structure)  
    const captured \= client.capturePlan(  
      'gpt-4',  
      'Find Coldplay concerts',  
      plan  // REQUIRED  
    );  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Parameters \[\#parameters\]

| Parameter | Type | Required | Description                                                             |  
| \--------- | \---- | \-------- | \----------------------------------------------------------------------- |  
| llm       | str  | Yes      | LLM identifier for context (e.g., "gpt-4", "claude-3", "gpt-3.5-turbo") |  
| prompt    | str  | Yes      | Natural language description of the task                                |  
| plan      | dict | \*\*Yes\*\*  | \*\*Required plan structure with \`goal\` and \`steps\` \- see below\*\*         |  
| metadata  | dict | No       | Optional metadata to attach to plan                                     |

Plan Structure \[\#plan-structure\]

The plan object must include:

\`\`\`json  
{  
    "goal": str,              // Required: High-level description  
    "steps": \[                // Required: Array of execution steps  
        {  
            "action": str,        // Required: Tool/action name from your MCP  
            "mcp": str,           // Required: Your onboarded MCP identifier    
            "params": dict,       // Optional: Tool parameters  
            "description": str,   // Optional: Human-readable description  
            "metadata": dict      // Optional: Additional metadata  
        }  
    \],  
    "metadata": dict          // Optional: Plan-level metadata  
}  
\`\`\`

\*\*Important\*\*: You must use the exact MCP identifiers and tool names from your onboarded MCPs on the ArmorIQ platform.

Returns \[\#returns\]

PlanCapture object containing:

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    {  
        "plan": dict,                  \# Your provided plan structure  
        "llm": str,                    \# LLM identifier used  
        "prompt": str,                 \# Original prompt  
        "metadata": dict               \# Attached metadata  
    }  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    interface PlanCapture {  
      plan: Record\<string, any\>;    // Your provided plan structure  
      llm?: string;                 // LLM identifier used  
      prompt?: string;              // Original prompt  
      metadata: Record\<string, any\> // Attached metadata  
    }  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Raises \[\#raises\]

\* ValueError/Error: If plan parameter is missing or invalid  
\* ValueError/Error: If required fields (\`goal\`, \`steps\`) are missing  
\* InvalidPlanError: If plan structure is malformed

Examples \[\#examples\]

Example 1: Single-Step Plan \[\#example-1-single-step-plan\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# Define a simple single-step plan  
    plan \= {  
        "goal": "Fetch user data from database",  
        "steps": \[  
            {  
                "action": "fetch\_user",  
                "mcp": "database-mcp",  
                "params": {"user\_id": "12345"}  
            }  
        \]  
    }

    captured \= client.capture\_plan(  
        llm="gpt-4",  
        prompt="Get user data for user 12345",  
        plan=plan  
    )

    print(f"Captured plan with {len(captured.plan\['steps'\])} step(s)")  
    print(f"Plan: {captured.plan}")  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    // Define a simple single-step plan  
    const plan \= {  
      goal: 'Fetch user data from database',  
      steps: \[  
        {  
          action: 'fetch\_user',  
          mcp: 'database-mcp',  
          params: { user\_id: '12345' }  
        }  
      \]  
    };

    const captured \= client.capturePlan(  
      'gpt-4',  
      'Get user data for user 12345',  
      plan  
    );

    console.log(\`Captured plan with ${captured.plan.steps?.length || 0} step(s)\`);  
    console.log('Plan:', captured.plan);  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Example 2: Multi-Step Plan \[\#example-2-multi-step-plan\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# Define a multi-step plan  
    multi\_step\_plan \= {  
        "goal": "Analyze user data and calculate risk score",  
        "steps": \[  
            {  
                "action": "fetch\_data",  
                "mcp": "data-mcp",  
                "params": {"user\_id": "12345"}  
            },  
            {  
                "action": "analyze",  
                "mcp": "analytics-mcp",  
                "params": {"metrics": \["risk\_score", "engagement"\]}  
            }  
        \]  
    }

    captured \= client.capture\_plan(  
        llm="gpt-4",  
        prompt="Fetch and analyze user data",  
        plan=multi\_step\_plan  
    )

    print(f"Captured {len(captured.plan\['steps'\])} steps")  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    // Define a multi-step plan  
    const multiStepPlan \= {  
      goal: 'Analyze user data and calculate risk score',  
      steps: \[  
        {  
          action: 'fetch\_data',  
          mcp: 'data-mcp',  
          params: { user\_id: '12345' }  
        },  
        {  
          action: 'analyze',  
          mcp: 'analytics-mcp',  
          params: { metrics: \['risk\_score', 'engagement'\] }  
        }  
      \]  
    };

    const captured \= client.capturePlan(  
      'gpt-4',  
      'Fetch and analyze user data',  
      multiStepPlan  
    );

    console.log(\`Captured ${captured.plan.steps?.length || 0} steps\`);  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Example 3: Plan with metadata \[\#example-3-plan-with-metadata\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# Include metadata for tracking  
    plan\_with\_metadata \= {  
        "goal": "Calculate credit risk for loan application",  
        "steps": \[  
            {  
                "action": "calculate\_risk",  
                "mcp": "analytics-mcp",  
                "description": "Calculate credit risk score",  
                "params": {"application\_id": "APP-12345"},  
                "metadata": {"priority": "high"}  
            }  
        \]  
    }

    captured \= client.capture\_plan(  
        llm="gpt-4",  
        prompt="Calculate credit risk for loan application",  
        plan=plan\_with\_metadata,  
        metadata={  
            "purpose": "credit\_assessment",  
            "version": "1.2.0",  
            "tags": \["finance", "risk"\]  
        }  
    )  
    print(f"Metadata: {captured.metadata}")  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    // Include metadata for tracking  
    const planWithMetadata \= {  
      goal: 'Calculate credit risk for loan application',  
      steps: \[  
        {  
          action: 'calculate\_risk',  
          mcp: 'analytics-mcp',  
          description: 'Calculate credit risk score',  
          params: { application\_id: 'APP-12345' },  
          metadata: { priority: 'high' }  
        }  
      \]  
    };

    const captured \= client.capturePlan(  
      'gpt-4',  
      'Calculate credit risk for loan application',  
      planWithMetadata,  
      {  
        purpose: 'credit\_assessment',  
        version: '1.2.0',  
        tags: \['finance', 'risk'\]  
      }  
    );  
    console.log('Metadata:', captured.metadata);  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

What happens during capture\_plan()? \[\#what-happens-during-capture\_plan\]

1\. \*\*SDK validates the plan structure\*\* you provide  
2\. \*\*Checks required fields\*\* (\`goal\`, \`steps\` array with \`action\` and \`mcp\` in each step)  
3\. \*\*Returns PlanCapture object\*\* with validated plan \- ready for \`get\_intent\_token()\`

\*\*Note\*\*: The SDK does NOT generate plans or call LLMs. You must provide the explicit plan structure based on your onboarded MCPs.

What happens AFTER capture\_plan()? \[\#what-happens-after-capture\_plan\]

When you call \`get\_intent\_token(plan\_capture)\`:

1\. \*\*Backend forwards plan to CSRG-IAP\*\*  
2\. \*\*CSRG-IAP canonicalizes the plan\*\* into CSRG format  
3\. \*\*Cryptographic hash computed\*\* (\`plan\_hash\`)  
4\. \*\*Merkle tree generated\*\* with \`merkle\_root\`  
5\. \*\*step\\\_proofs array created\*\* \- one Merkle proof for EACH step  
6\. \*\*Token signed with Ed25519\*\*  
7\. \*\*Token returned\*\* with \`plan\_hash\`, \`merkle\_root\`, and \`step\_proofs\[\]\`

The \`step\_proofs\` array is used later during \`invoke()\` \- the SDK extracts the appropriate proof and sends it in the \`X-CSRG-Proof\` header for verification.

\# capture\_plan()

\*\*Design Philosophy\*\*: It captures the agent's intent by accepting an explicit plan structure. You define which MCPs and actions the agent will execute. The SDK validates the plan structure, then CSRG-IAP creates the cryptographic proof. This is the foundation of ArmorIQ's intent-based security model.

Captures and validates an execution plan structure. The plan must explicitly define the steps the agent intends to execute based on your onboarded MCPs.

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    client.capture\_plan(  
        llm: str,  
        prompt: str,  
        plan: dict,              \# REQUIRED  
        metadata: dict \= None  
    ) \-\> PlanCapture  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    client.capturePlan(  
      llm: string,  
      prompt: string,  
      plan: Record\<string, any\>,  // REQUIRED  
      metadata?: Record\<string, any\>  
    ): PlanCapture  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Required Plan Structure \[\#required-plan-structure\]

You must provide an explicit plan with your onboarded MCPs and their tools:

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# Define your execution plan  
    plan \= {  
        "goal": "Search for Coldplay concerts",  \# Required: what you want to accomplish  
        "steps": \[                                \# Required: array of actions  
            {  
                "action": "search\_events",        \# Tool name from your MCP  
                "mcp": "ticketmaster-mcp",       \# Your onboarded MCP identifier  
                "params": {"artist": "Coldplay"}  \# Tool parameters  
            }  
        \]  
    }

    \# Capture the plan (SDK validates structure)  
    captured \= client.capture\_plan(  
        llm="gpt-4",  
        prompt="Find Coldplay concerts",  
        plan=plan  \# REQUIRED  
    )  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    // Define your execution plan  
    const plan \= {  
      goal: 'Search for Coldplay concerts',   // Required: what you want to accomplish  
      steps: \[                                 // Required: array of actions  
        {  
          action: 'search\_events',            // Tool name from your MCP  
          mcp: 'ticketmaster-mcp',           // Your onboarded MCP identifier  
          params: { artist: 'Coldplay' }      // Tool parameters  
        }  
      \]  
    };

    // Capture the plan (SDK validates structure)  
    const captured \= client.capturePlan(  
      'gpt-4',  
      'Find Coldplay concerts',  
      plan  // REQUIRED  
    );  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Parameters \[\#parameters\]

| Parameter | Type | Required | Description                                                             |  
| \--------- | \---- | \-------- | \----------------------------------------------------------------------- |  
| llm       | str  | Yes      | LLM identifier for context (e.g., "gpt-4", "claude-3", "gpt-3.5-turbo") |  
| prompt    | str  | Yes      | Natural language description of the task                                |  
| plan      | dict | \*\*Yes\*\*  | \*\*Required plan structure with \`goal\` and \`steps\` \- see below\*\*         |  
| metadata  | dict | No       | Optional metadata to attach to plan                                     |

Plan Structure \[\#plan-structure\]

The plan object must include:

\`\`\`json  
{  
    "goal": str,              // Required: High-level description  
    "steps": \[                // Required: Array of execution steps  
        {  
            "action": str,        // Required: Tool/action name from your MCP  
            "mcp": str,           // Required: Your onboarded MCP identifier    
            "params": dict,       // Optional: Tool parameters  
            "description": str,   // Optional: Human-readable description  
            "metadata": dict      // Optional: Additional metadata  
        }  
    \],  
    "metadata": dict          // Optional: Plan-level metadata  
}  
\`\`\`

\*\*Important\*\*: You must use the exact MCP identifiers and tool names from your onboarded MCPs on the ArmorIQ platform.

Returns \[\#returns\]

PlanCapture object containing:

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    {  
        "plan": dict,                  \# Your provided plan structure  
        "llm": str,                    \# LLM identifier used  
        "prompt": str,                 \# Original prompt  
        "metadata": dict               \# Attached metadata  
    }  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    interface PlanCapture {  
      plan: Record\<string, any\>;    // Your provided plan structure  
      llm?: string;                 // LLM identifier used  
      prompt?: string;              // Original prompt  
      metadata: Record\<string, any\> // Attached metadata  
    }  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Raises \[\#raises\]

\* ValueError/Error: If plan parameter is missing or invalid  
\* ValueError/Error: If required fields (\`goal\`, \`steps\`) are missing  
\* InvalidPlanError: If plan structure is malformed

Examples \[\#examples\]

Example 1: Single-Step Plan \[\#example-1-single-step-plan\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# Define a simple single-step plan  
    plan \= {  
        "goal": "Fetch user data from database",  
        "steps": \[  
            {  
                "action": "fetch\_user",  
                "mcp": "database-mcp",  
                "params": {"user\_id": "12345"}  
            }  
        \]  
    }

    captured \= client.capture\_plan(  
        llm="gpt-4",  
        prompt="Get user data for user 12345",  
        plan=plan  
    )

    print(f"Captured plan with {len(captured.plan\['steps'\])} step(s)")  
    print(f"Plan: {captured.plan}")  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    // Define a simple single-step plan  
    const plan \= {  
      goal: 'Fetch user data from database',  
      steps: \[  
        {  
          action: 'fetch\_user',  
          mcp: 'database-mcp',  
          params: { user\_id: '12345' }  
        }  
      \]  
    };

    const captured \= client.capturePlan(  
      'gpt-4',  
      'Get user data for user 12345',  
      plan  
    );

    console.log(\`Captured plan with ${captured.plan.steps?.length || 0} step(s)\`);  
    console.log('Plan:', captured.plan);  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Example 2: Multi-Step Plan \[\#example-2-multi-step-plan\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# Define a multi-step plan  
    multi\_step\_plan \= {  
        "goal": "Analyze user data and calculate risk score",  
        "steps": \[  
            {  
                "action": "fetch\_data",  
                "mcp": "data-mcp",  
                "params": {"user\_id": "12345"}  
            },  
            {  
                "action": "analyze",  
                "mcp": "analytics-mcp",  
                "params": {"metrics": \["risk\_score", "engagement"\]}  
            }  
        \]  
    }

    captured \= client.capture\_plan(  
        llm="gpt-4",  
        prompt="Fetch and analyze user data",  
        plan=multi\_step\_plan  
    )

    print(f"Captured {len(captured.plan\['steps'\])} steps")  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    // Define a multi-step plan  
    const multiStepPlan \= {  
      goal: 'Analyze user data and calculate risk score',  
      steps: \[  
        {  
          action: 'fetch\_data',  
          mcp: 'data-mcp',  
          params: { user\_id: '12345' }  
        },  
        {  
          action: 'analyze',  
          mcp: 'analytics-mcp',  
          params: { metrics: \['risk\_score', 'engagement'\] }  
        }  
      \]  
    };

    const captured \= client.capturePlan(  
      'gpt-4',  
      'Fetch and analyze user data',  
      multiStepPlan  
    );

    console.log(\`Captured ${captured.plan.steps?.length || 0} steps\`);  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Example 3: Plan with metadata \[\#example-3-plan-with-metadata\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# Include metadata for tracking  
    plan\_with\_metadata \= {  
        "goal": "Calculate credit risk for loan application",  
        "steps": \[  
            {  
                "action": "calculate\_risk",  
                "mcp": "analytics-mcp",  
                "description": "Calculate credit risk score",  
                "params": {"application\_id": "APP-12345"},  
                "metadata": {"priority": "high"}  
            }  
        \]  
    }

    captured \= client.capture\_plan(  
        llm="gpt-4",  
        prompt="Calculate credit risk for loan application",  
        plan=plan\_with\_metadata,  
        metadata={  
            "purpose": "credit\_assessment",  
            "version": "1.2.0",  
            "tags": \["finance", "risk"\]  
        }  
    )  
    print(f"Metadata: {captured.metadata}")  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    // Include metadata for tracking  
    const planWithMetadata \= {  
      goal: 'Calculate credit risk for loan application',  
      steps: \[  
        {  
          action: 'calculate\_risk',  
          mcp: 'analytics-mcp',  
          description: 'Calculate credit risk score',  
          params: { application\_id: 'APP-12345' },  
          metadata: { priority: 'high' }  
        }  
      \]  
    };

    const captured \= client.capturePlan(  
      'gpt-4',  
      'Calculate credit risk for loan application',  
      planWithMetadata,  
      {  
        purpose: 'credit\_assessment',  
        version: '1.2.0',  
        tags: \['finance', 'risk'\]  
      }  
    );  
    console.log('Metadata:', captured.metadata);  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

What happens during capture\_plan()? \[\#what-happens-during-capture\_plan\]

1\. \*\*SDK validates the plan structure\*\* you provide  
2\. \*\*Checks required fields\*\* (\`goal\`, \`steps\` array with \`action\` and \`mcp\` in each step)  
3\. \*\*Returns PlanCapture object\*\* with validated plan \- ready for \`get\_intent\_token()\`

\*\*Note\*\*: The SDK does NOT generate plans or call LLMs. You must provide the explicit plan structure based on your onboarded MCPs.

What happens AFTER capture\_plan()? \[\#what-happens-after-capture\_plan\]

When you call \`get\_intent\_token(plan\_capture)\`:

1\. \*\*Backend forwards plan to CSRG-IAP\*\*  
2\. \*\*CSRG-IAP canonicalizes the plan\*\* into CSRG format  
3\. \*\*Cryptographic hash computed\*\* (\`plan\_hash\`)  
4\. \*\*Merkle tree generated\*\* with \`merkle\_root\`  
5\. \*\*step\\\_proofs array created\*\* \- one Merkle proof for EACH step  
6\. \*\*Token signed with Ed25519\*\*  
7\. \*\*Token returned\*\* with \`plan\_hash\`, \`merkle\_root\`, and \`step\_proofs\[\]\`

The \`step\_proofs\` array is used later during \`invoke()\` \- the SDK extracts the appropriate proof and sends it in the \`X-CSRG-Proof\` header for verification.

\# Policy Specification

Policy Specification \[\#policy-specification\]

Policies can be defined programmatically (in the SDK) or visually (ArmorIQ Canvas).

Policy Structure \[\#policy-structure\]

\`\`\`json  
{  
    "allow": list\[str\],            \# Allowed actions (glob patterns, e.g., "analytics-mcp/\*")  
    "deny": list\[str\],             \# Denied actions (glob patterns, e.g., "data-mcp/delete\_\*")  
    "allowed\_tools": list\[str\],    \# Whitelisted tool names (optional)  
    "rate\_limit": int,             \# Requests per hour (optional)  
    "ip\_whitelist": list\[str\],     \# Allowed IPs/CIDR ranges (optional)  
    "time\_restrictions": {         \# Time-based access (optional)  
        "allowed\_hours": list\[int\],    \# 0-23 (e.g., \[9, 10, 11, ..., 17\] for 9 AM \- 5 PM)  
        "allowed\_days": list\[str\]      \# \["Monday", "Tuesday", ...\]  
    },  
    "priority": int                \# Policy priority 0-100 (higher \= more important)  
}  
\`\`\`

Method 1: Programmatic (SDK) \[\#method-1-programmatic-sdk\]

\`\`\`python  
policy \= {  
    "allow": \["analytics-mcp/\*", "data-mcp/fetch\_\*"\],  
    "deny": \["data-mcp/delete\_\*"\],  
    "allowed\_tools": \["read\_file", "analyze", "aggregate"\],  
    "rate\_limit": 100,  
    "ip\_whitelist": \["10.0.0.0/8"\],  
    "time\_restrictions": {  
        "allowed\_hours": \[9, 10, 11, 12, 13, 14, 15, 16, 17\],  
        "allowed\_days": \["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"\]  
    }  
}

token \= client.get\_intent\_token(  
    plan\_capture=plan,  
    policy=policy,  
    validity\_seconds=3600  
)  
\`\`\`

Method 2: Visual Policy Builder (ArmorIQ Canvas) \[\#method-2-visual-policy-builder-armoriq-canvas\]

Use the drag-and-drop interface at \[https://platform.armoriq.ai/dashboard/policies\](https://platform.armoriq.ai/dashboard/policies):

1\. Click "Canvas" button to open visual builder  
2\. Drag users, MCPs, and agents onto canvas  
3\. Connect entities with edges (connections)  
4\. Click edge to configure permissions visually  
5\. Use "Browse Tools" to select allowed tools from MCP  
6\. Set IP restrictions, time windows, rate limits  
7\. Save policy with name and priority

Use policy ID in SDK:

\`\`\`python  
\# Use policy created in Canvas  
token \= client.get\_intent\_token(  
    plan\_capture=plan,  
    policy\_id="f88cf4c7-732d-44ff-901b-fd3d882c2ecf",  \# From Canvas  
    validity\_seconds=3600  
)

\# Or fetch policy JSON from API and use directly  
import requests  
policy\_response \= requests.get(  
   f"https://customer-api.armoriq.ai/policies/f88cf4c7-732d-44ff-901b-fd3d882c2ecf",  
   headers={"Authorization": f"Bearer {user\_jwt}"}  
)  
policy \= policy\_response.json()\["data"\]\["permissions"\]

token \= client.get\_intent\_token(  
    plan\_capture=plan,  
    policy=policy,  
    validity\_seconds=3600  
)  
\`\`\`

Policy Encoding \[\#policy-encoding\]

The policy is automatically encoded into the CSRG token JWT payload and cryptographically verified during execution. The proxy enforces policy rules before routing requests to MCPs.

\# invoke()

Executes an action on an MCP server with cryptographic verification.

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    client.invoke(  
        mcp: str,  
        action: str,  
        intent\_token: IntentToken,  
        params: dict \= None,  
        merkle\_proof: list \= None,  
        user\_email: str \= None  
    ) \-\> MCPInvocationResult  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    await client.invoke(  
      mcp: string,  
      action: string,  
      intentToken: IntentToken,  
      params?: Record\<string, any\>,  
      merkleProof?: Array\<Record\<string, any\>\>,  
      userEmail?: string  
    ): Promise\<MCPInvocationResult\>  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Parameters \[\#parameters\]

| Parameter     | Type        | Required | Default        | Description                              |  
| \------------- | \----------- | \-------- | \-------------- | \---------------------------------------- |  
| mcp           | str         | Yes      | \-              | MCP server name (e.g., "analytics-mcp")  |  
| action        | str         | Yes      | \-              | Action/tool to execute (must be in plan) |  
| intent\\\_token | IntentToken | Yes      | \-              | Token from get\\\_intent\\\_token()          |  
| params        | dict        | No       | {}             | Action parameters                        |  
| merkle\\\_proof | list        | No       | Auto-generated | Optional Merkle proof                    |  
| user\\\_email   | str         | No       | None           | Optional user email                      |

Flow \[\#flow\]

1\. SDK generates Merkle proof for this action from plan  
2\. SDK → ArmorIQ Proxy POST /invoke with CSRG headers:  
   \* X-API-Key: API key for authentication  
   \* X-CSRG-Path: Path in plan (e.g., /steps/\\\[0\]/action)  
   \* X-CSRG-Value-Digest: SHA256 hash of action value  
   \* X-CSRG-Proof: JSON Merkle proof array  
3\. Proxy performs IAP Step Verification:  
   \* Validates Merkle proof against plan\\\_hash  
   \* Verifies CSRG path matches plan structure  
   \* Checks value digest matches action  
   \* Verifies Ed25519 signature on token  
4\. If verification passes, proxy routes to MCP server  
5\. MCP executes action and returns result

Returns \[\#returns\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    {  
        "success": bool,               \# Whether action succeeded  
        "data": any,                   \# Response data from MCP  
        "error": str,                  \# Error message (if failed)  
        "execution\_time\_ms": int,      \# Execution duration  
        "mcp": str,                    \# MCP that executed  
        "action": str                  \# Action that ran  
    }  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    interface MCPInvocationResult {  
      mcp: string;                  // MCP identifier  
      action: string;               // Action that was invoked  
      result: any;                  // Action result data  
      status: string;               // Execution status  
      executionTime?: number;       // Time taken (seconds)  
      verified: boolean;            // Token verification status  
      metadata: Record\<string, any\> // Extra metadata  
    }  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Raises \[\#raises\]

\* VerificationError: If IAP Step Verification fails  
\* TokenExpiredError: If token has expired  
\* MCPError: If MCP execution fails  
\* NetworkError: If request fails

Example \[\#example\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# Basic invocation  
    result \= client.invoke(  
        mcp="analytics-mcp",  
        action="analyze",  
        intent\_token=token,  
        params={"data": \[1, 2, 3, 4, 5\], "metrics": \["mean", "std"\]}  
    )

    if result\["success"\]:  
        print(f"Results: {result\['data'\]}")  
        print(f"Took: {result\['execution\_time\_ms'\]}ms")  
    else:  
        print(f"Error: {result\['error'\]}")

    \# With error handling  
    try:  
        result \= client.invoke("data-mcp", "fetch\_data", token, {"source": "db"})

        if result\["success"\]:  
            data \= result\["data"\]  
        else:  
            logger.error(f"MCP error: {result\['error'\]}")

    except TokenExpiredError:  
        \# Get fresh token  
        token \= client.get\_intent\_token(plan)\["token"\]  
        result \= client.invoke("data-mcp", "fetch\_data", token, {"source": "db"})

    except VerificationError as e:  
        \# Action not in plan  
        logger.error(f"Verification failed: {e}")  
        \# Need to recreate plan with correct actions

    \# Custom timeout  
    result \= client.invoke(  
        "analytics-mcp",  
        "long\_analysis",  
        token,  
        {"dataset": "large"},  
        timeout=120  \# 2 minutes  
    )  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import {   
      ArmorIQClient,   
      TokenExpiredException,   
      IntentMismatchException   
    } from '@armoriq/sdk';

    // Basic invocation  
    const result \= await client.invoke(  
      'analytics-mcp',  
      'analyze',  
      token,  
      { data: \[1, 2, 3, 4, 5\], metrics: \['mean', 'std'\] }  
    );

    console.log(\`Results: ${JSON.stringify(result.result)}\`);  
    console.log(\`Took: ${result.executionTime?.toFixed(2)}s\`);

    // With error handling  
    try {  
      const result \= await client.invoke(  
        'data-mcp',  
        'fetch\_data',  
        token,  
        { source: 'db' }  
      );  
      const data \= result.result;  
    } catch (error) {  
      if (error instanceof TokenExpiredException) {  
        // Get fresh token  
        const newToken \= await client.getIntentToken(planCapture);  
        const result \= await client.invoke(  
          'data-mcp',  
          'fetch\_data',  
          newToken,  
          { source: 'db' }  
        );  
      } else if (error instanceof IntentMismatchException) {  
        // Action not in plan  
        console.error(\`Verification failed: ${error.message}\`);  
        // Need to recreate plan with correct actions  
      }  
    }

    // Sequential invocation from complete workflow  
    const result1 \= await client.invoke('weather-mcp', 'get\_weather', token, { city: 'Boston' });  
    console.log(\`Boston weather: ${JSON.stringify(result1.result)}\`);

    const result2 \= await client.invoke('weather-mcp', 'get\_weather', token, { city: 'New York' });  
    console.log(\`New York weather: ${JSON.stringify(result2.result)}\`);  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

\# delegate()

Delegate authority to another agent using cryptographic token delegation. This allows an agent to grant temporary, restricted access to a sub-agent for executing specific subtasks.

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    client.delegate(  
        intent\_token: IntentToken,  
        delegate\_public\_key: str,  
        validity\_seconds: int \= 3600,  
        allowed\_actions: list \= None,  
        subtask: dict \= None  
    ) \-\> DelegationResult  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    await client.delegate(  
      intentToken: IntentToken,  
      delegatePublicKey: string,  
      validitySeconds?: number,  // default: 3600  
      allowedActions?: string\[\],  
      targetAgent?: string,  
      subtask?: Record\<string, any\>  
    ): Promise\<DelegationResult\>  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Parameters \[\#parameters\]

| Parameter             | Type        | Required | Default | Description                                                 |  
| \--------------------- | \----------- | \-------- | \------- | \----------------------------------------------------------- |  
| intent\\\_token         | IntentToken | Yes      | \-       | Parent agent's intent token to delegate                     |  
| delegate\\\_public\\\_key | str         | Yes      | \-       | Ed25519 public key of delegate agent (hex format)           |  
| validity\\\_seconds     | int         | No       | 3600    | Delegation token validity in seconds                        |  
| allowed\\\_actions      | list        | No       | None    | List of allowed actions (defaults to all from parent token) |  
| subtask               | dict        | No       | None    | Optional subtask plan structure                             |

Returns \[\#returns\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    {  
        "delegation\_id": str,           \# Unique delegation identifier  
        "delegated\_token": IntentToken, \# New token for delegate agent  
        "delegate\_public\_key": str,     \# Public key of delegate  
        "expires\_at": float,            \# Unix timestamp of expiration  
        "trust\_delta": dict,            \# Trust update applied  
        "status": str                   \# Delegation status  
    }  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    interface DelegationResult {  
      delegationId: string;             // Unique delegation identifier  
      delegatedToken: IntentToken;      // New token for delegate agent  
      delegatePublicKey: string;        // Public key of delegate  
      targetAgent?: string;             // Optional target agent identifier  
      expiresAt: number;                // Unix timestamp of expiration  
      trustDelta: Record\<string, any\>;  // Trust update applied  
      status: string;                   // Delegation status  
      metadata: Record\<string, any\>;    // Extra metadata  
    }  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Raises \[\#raises\]

\* DelegationException: If delegation creation fails  
\* InvalidTokenException: If parent token is invalid or expired  
\* AuthenticationError: If IAP endpoint is unreachable

Flow \[\#flow\]

1\. Parent agent creates main plan and gets token  
2\. Parent calls delegate() with delegate's public key  
3\. SDK → CSRG-IAP POST /delegation/create  
4\. IAP creates new token with:  
   \* Restricted permissions (if allowed\\\_actions specified)  
   \* Delegate's public key bound cryptographically  
   \* Shorter validity period  
5\. Delegated token returned to parent  
6\. Parent sends delegated token to sub-agent  
7\. Sub-agent uses delegated token for authorized actions only

Example \[\#example\]

Basic Delegation \[\#basic-delegation\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    from cryptography.hazmat.primitives.asymmetric import ed25519  
    from cryptography.hazmat.primitives import serialization

    \# Generate keypair for delegate agent  
    delegate\_private\_key \= ed25519.Ed25519PrivateKey.generate()  
    delegate\_public\_key \= delegate\_private\_key.public\_key()

    \# Convert public key to hex format  
    pub\_key\_bytes \= delegate\_public\_key.public\_bytes(  
        encoding=serialization.Encoding.Raw,  
        format=serialization.PublicFormat.Raw  
    )  
    pub\_key\_hex \= pub\_key\_bytes.hex()

    \# Delegate authority  
    delegation\_result \= client.delegate(  
        intent\_token=parent\_token,  
        delegate\_public\_key=pub\_key\_hex,  
        validity\_seconds=1800,  \# 30 minutes  
        allowed\_actions=\["book\_venue", "arrange\_catering"\]  
    )

    print(f"✅ Delegation created: {delegation\_result.delegation\_id}")  
    print(f"Delegated token: {delegation\_result.delegated\_token.token\_id}")

    \# Send delegated token to sub-agent  
    sub\_agent\_client.invoke(  
        "events-mcp",  
        "book\_venue",  
        delegation\_result.delegated\_token,  
        {"venue\_id": "v123", "date": "2026-04-15"}  
    )  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import \* as crypto from 'crypto';  
    import { ArmorIQClient, DelegationException } from '@armoriq/sdk';

    // Generate keypair for delegate agent  
    const { publicKey, privateKey } \= crypto.generateKeyPairSync('ed25519');

    // Convert public key to hex format  
    const pubKeyHex \= publicKey  
      .export({ type: 'spki', format: 'der' })  
      .toString('hex');

    // Delegate authority  
    try {  
      const delegationResult \= await client.delegate(  
        parentToken,  
        pubKeyHex,  
        1800,  // 30 minutes validity  
        \['book\_venue', 'arrange\_catering'\],  // allowed actions  
        'sub-agent-1'  // target agent identifier  
      );

      console.log(\`✅ Delegation created: ${delegationResult.delegationId}\`);  
      console.log(\`Delegated token: ${delegationResult.delegatedToken.tokenId}\`);

      // Send delegated token to sub-agent  
      await subAgentClient.invoke(  
        'events-mcp',  
        'book\_venue',  
        delegationResult.delegatedToken,  
        { venue\_id: 'v123', date: '2026-04-15' }  
      );  
    } catch (error) {  
      if (error instanceof DelegationException) {  
        console.error(\`Delegation failed: ${error.message}\`);  
      }  
    }  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Delegation Chain (Hierarchical) \[\#delegation-chain-hierarchical\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# Level 1: Manager delegates to Team Lead  
    lead\_delegation \= manager\_client.delegate(  
        manager\_token,  
        delegate\_public\_key=team\_lead\_pubkey,  
        validity\_seconds=7200  
    )

    \# Level 2: Team Lead delegates to Specialist  
    specialist\_delegation \= team\_lead\_client.delegate(  
        lead\_delegation.delegated\_token,  \# Use delegated token  
        delegate\_public\_key=specialist\_pubkey,  
        validity\_seconds=3600,  
        allowed\_actions=\["execute\_subtask"\]  \# Further restricted  
    )  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    // Level 1: Manager delegates to Team Lead  
    const leadDelegation \= await managerClient.delegate(  
      managerToken,  
      teamLeadPubkey,  
      7200  // 2 hours  
    );

    // Level 2: Team Lead delegates to Specialist  
    const specialistDelegation \= await teamLeadClient.delegate(  
      leadDelegation.delegatedToken,  // Use delegated token  
      specialistPubkey,  
      3600,  // 1 hour  
      \['execute\_subtask'\]  // Further restricted  
    );  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Security Properties \[\#security-properties\]

\* \*\*Cryptographically Bound\*\*: Delegation is signed with IAP's Ed25519 key  
\* \*\*Non-transferable\*\*: Delegate cannot re-delegate without explicit permission  
\* \*\*Time-Limited\*\*: Delegated tokens expire faster than parent tokens  
\* \*\*Action-Restricted\*\*: Delegate can only execute allowed actions  
\* \*\*Auditable\*\*: All delegations logged with delegation\\\_id and trust\\\_delta  
\* \*\*Revocable\*\*: Parent token expiration invalidates all delegations

\# Data Models

Data Models \[\#data-models\]

Each data model has its own page. Use the links below to jump directly to the model you need.

Models \[\#models\]

\* \[IntentPlan\](/docs/data-models/intent-plan)  
\* \[IntentToken\](/docs/data-models/intent-token)  
\* \[MCPResult\](/docs/data-models/mcp-result)

\# IntentPlan

IntentPlan \[\#intentplan\]

Returned by \`capture\_plan()\`.

\`\`\`json  
{  
    "canonical\_plan": {  
        "graph": {  
            "steps": \[  
                {  
                    "action": str,  
                    "mcp": str,  
                    "index": int,  
                    "path": str,  
                    "value\_digest": str  
                }  
            \],  
            "metadata": {  
                "canonical\_version": str,  
                "plan\_hash": str,  
                "created\_at": str  
            }  
        }  
    },  
    "plan\_hash": str,  
    "merkle\_tree": {  
        "root": str,  
        "leaves": list\[str\],  
        "proofs": dict  
    },  
    "created\_at": str  
}  
\`\`\`

\# IntentToken

IntentToken \[\#intenttoken\]

Returned by \`get\_intent\_token()\`.

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`json  
    {  
        "success": bool,  
        "token": str,                  \# JWT format: header.payload.signature  
        "plan\_hash": str,              \# SHA-256: "sha256:abc123..."  
        "merkle\_root": str,            \# SHA-256: "sha256:def456..."  
        "expires\_at": int,             \# Unix timestamp  
        "issued\_at": int               \# Unix timestamp  
    }  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    interface IntentToken {  
      tokenId: string;              // Unique identifier (intent\_reference)  
      planHash: string;             // CSRG hash of the canonical plan  
      planId?: string;              // Plan ID from IAP  
      signature: string;            // Ed25519 signature from IAP  
      issuedAt: number;             // Unix timestamp  
      expiresAt: number;            // Unix timestamp  
      policy: Record\<string, any\>;  // Policy manifest  
      compositeIdentity: string;    // Composite identity hash  
      stepProofs: Array\<any\>;       // Merkle proofs for each step  
      totalSteps: number;           // Total number of steps  
      rawToken: Record\<string, any\>; // Full raw token payload  
      jwtToken?: string;            // JWT token for verify-step endpoint  
    }

    // Helper functions  
    namespace IntentToken {  
      function isExpired(token: IntentToken): boolean;  
      function timeUntilExpiry(token: IntentToken): number;  
    }  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Token JWT Payload \[\#token-jwt-payload\]

\`\`\`json  
{  
    "iss": "armoriq-csrg-iap",  
    "sub": "user\_001",  
    "aud": "armoriq-proxy",  
    "iat": 1737454200,  
    "exp": 1737457800,  
    "plan\_hash": "sha256:...",  
    "merkle\_root": "sha256:...",  
    "policy": {"allow": \["\*"\], "deny": \[\]},  
    "identity": {  
        "user\_id": "user\_001",  
        "agent\_id": "my\_agent",  
        "api\_key\_id": "key\_789"  
    }  
}  
\`\`\`

\# MCPResult

MCPResult \[\#mcpresult\]

Returned by \`invoke()\`.

\`\`\`json  
{  
    "success": bool,  
    "data": any,                   \# MCP-specific response  
    "error": str,                  \# Present if success=False  
    "execution\_time\_ms": int,  
    "mcp": str,  
    "action": str  
}  
\`\`\`

\# MCP Registry

MCP Registry \[\#mcp-registry\]

The MCP Registry allows you to register and manage your Model Context Protocol (MCP) servers with the ArmorIQ platform.

Building Your Own MCP \[\#building-your-own-mcp\]

Want to create your own MCP for ArmorIQ SDK? Check out the \[MCP Format Requirements\](./mcp-format) guide to learn the exact protocol specifications needed.

Registering Your MCP \[\#registering-your-mcp\]

Once you've built your MCP following the format requirements, register it with the platform:

Step 1: Login to Platform \[\#step-1-login-to-platform\]

Navigate to \[platform.armoriq.ai\](https://platform.armoriq.ai) and sign in with your credentials.

Step 2: Navigate to MCP Registry \[\#step-2-navigate-to-mcp-registry\]

Go to the MCP Registry section in the platform dashboard.

Step 3: Add Your MCP \[\#step-3-add-your-mcp\]

Click on "Add MCP" and provide:

\* \*\*MCP Name\*\*: A unique identifier for your MCP (e.g., \`analytics-mcp\`, \`finance-mcp\`)  
\* \*\*MCP URL\*\*: Your HTTPS endpoint (e.g., \`https://your-mcp.example.com/mcp\`)

Step 4: Onboard to Platform \[\#step-4-onboard-to-platform\]

Submit the form to onboard your MCP to the ArmorIQ platform. Your MCP will be validated and made available for use.

Using Your MCP with ArmorIQ SDK \[\#using-your-mcp-with-armoriq-sdk\]

Once registered, you can access your MCP from the ArmorIQ SDK using the \*\*exact same name\*\* you registered:

\`\`\`python  
from armoriq\_sdk import ArmorIQClient

client \= ArmorIQClient(  
    api\_key="ak\_live\_...",  
    user\_id="user\_123",  
    agent\_id="my\_agent"  
)

\# Create a plan that uses your registered MCP  
plan \= client.capture\_plan(  
    prompt="Analyze user behavior data",  
    mcp\_actions=\[  
        {  
            "mcp": "analytics-mcp",  \# Use the exact name you registered  
            "action": "analyze",  
            "parameters": {  
                "data\_source": "user\_events"  
            }  
        }  
    \]  
)

\# Get token and delegate  
token \= client.get\_intent\_token(plan\_capture=plan)  
result \= client.delegate(token)  
\`\`\`

\*\*Important\*\*: The MCP name in your SDK calls must match exactly with the name you used during registration on the platform.

\# MCP Format Requirements

MCP Format Requirements \[\#mcp-format-requirements\]

This guide outlines the exact format requirements for building Model Context Protocol (MCP) servers that integrate with the ArmorIQ SDK.

Protocol Requirements \[\#protocol-requirements\]

Transport Protocol \[\#transport-protocol\]

\* \*\*Protocol\*\*: JSON-RPC 2.0 over HTTP  
\* \*\*Response Format\*\*: Server-Sent Events (SSE)  
\* \*\*Endpoint\*\*: Must expose a POST endpoint (e.g., \`/mcp\`)  
\* \*\*Content-Type\*\*: \`application/json\` for requests  
\* \*\*Response Type\*\*: \`text/event-stream\` for responses

SSE Response Format \[\#sse-response-format\]

All JSON-RPC responses must be wrapped in SSE format:

\`\`\`  
event: message  
data: {json-rpc-response}

\`\`\`

\*\*Note\*\*: The double newline at the end is required.

Required Methods \[\#required-methods\]

1\. initialize \[\#1-initialize\]

Handshake between client and server.

\*\*Request\*\*:

\`\`\`json  
{  
  "jsonrpc": "2.0",  
  "id": 1,  
  "method": "initialize",  
  "params": {  
    "protocolVersion": "2024-11-05",  
    "capabilities": {},  
    "clientInfo": {  
      "name": "armoriq-agent",  
      "version": "1.0.0"  
    }  
  }  
}  
\`\`\`

\*\*Response\*\*:

\`\`\`json  
{  
  "jsonrpc": "2.0",  
  "id": 1,  
  "result": {  
    "protocolVersion": "2024-11-05",  
    "capabilities": {  
      "tools": {}  
    },  
    "serverInfo": {  
      "name": "your-mcp-server-name",  
      "version": "1.0.0"  
    }  
  }  
}  
\`\`\`

2\. tools/list \[\#2-toolslist\]

Return list of available tools.

\*\*Request\*\*:

\`\`\`json  
{  
  "jsonrpc": "2.0",  
  "id": 2,  
  "method": "tools/list"  
}  
\`\`\`

\*\*Response\*\*:

\`\`\`json  
{  
  "jsonrpc": "2.0",  
  "id": 2,  
  "result": {  
    "tools": \[  
      {  
        "name": "tool\_name",  
        "description": "Clear description of what this tool does",  
        "inputSchema": {  
          "type": "object",  
          "properties": {  
            "parameter1": {  
              "type": "string",  
              "description": "Description of parameter1"  
            }  
          },  
          "required": \["parameter1"\]  
        }  
      }  
    \]  
  }  
}  
\`\`\`

3\. tools/call \[\#3-toolscall\]

Execute a specific tool.

\*\*Request\*\*:

\`\`\`json  
{  
  "jsonrpc": "2.0",  
  "id": 3,  
  "method": "tools/call",  
  "params": {  
    "name": "tool\_name",  
    "arguments": {  
      "parameter1": "value1"  
    }  
  }  
}  
\`\`\`

\*\*Response\*\*:

\`\`\`json  
{  
  "jsonrpc": "2.0",  
  "id": 3,  
  "result": {  
    "content": \[  
      {  
        "type": "text",  
        "text": "{\\"result\\": \\"your data here\\"}"  
      }  
    \]  
  }  
}  
\`\`\`

\*\*Important\*\*:

\* The \`content\` field must be an array  
\* Each item must have \`type: "text"\`  
\* The actual data must be a JSON string in the \`text\` field  
\* Do NOT return raw objects in \`text\`, stringify them first

Python Implementation Example \[\#python-implementation-example\]

\`\`\`python  
from fastapi import FastAPI, Request  
from fastapi.responses import StreamingResponse  
import json

app \= FastAPI()

TOOLS \= \[  
    {  
        "name": "example\_tool",  
        "description": "Example tool description",  
        "inputSchema": {  
            "type": "object",  
            "properties": {  
                "query": {  
                    "type": "string",  
                    "description": "Query parameter"  
                }  
            },  
            "required": \["query"\]  
        }  
    }  
\]

def sse\_response(data):  
    """Format response as SSE"""  
    json\_str \= json.dumps(data)  
    return f"event: message\\ndata: {json\_str}\\n\\n"

async def handle\_jsonrpc(request\_data):  
    method \= request\_data.get("method")  
    msg\_id \= request\_data.get("id")  
      
    if method \== "initialize":  
        return {  
            "jsonrpc": "2.0",  
            "id": msg\_id,  
            "result": {  
                "protocolVersion": "2024-11-05",  
                "capabilities": {"tools": {}},  
                "serverInfo": {  
                    "name": "example-mcp",  
                    "version": "1.0.0"  
                }  
            }  
        }  
      
    elif method \== "tools/list":  
        return {  
            "jsonrpc": "2.0",  
            "id": msg\_id,  
            "result": {"tools": TOOLS}  
        }  
      
    elif method \== "tools/call":  
        tool\_name \= request\_data\["params"\]\["name"\]  
        arguments \= request\_data\["params"\]\["arguments"\]  
          
        \# Execute your tool logic here  
        result\_data \= {"result": "processed data"}  
          
        return {  
            "jsonrpc": "2.0",  
            "id": msg\_id,  
            "result": {  
                "content": \[  
                    {  
                        "type": "text",  
                        "text": json.dumps(result\_data)  
                    }  
                \]  
            }  
        }

@app.post("/mcp")  
async def mcp\_endpoint(request: Request):  
    request\_data \= await request.json()  
    response\_data \= await handle\_jsonrpc(request\_data)  
      
    async def stream():  
        yield sse\_response(response\_data)  
      
    return StreamingResponse(  
        stream(),  
        media\_type="text/event-stream"  
    )  
\`\`\`

Deployment Requirements \[\#deployment-requirements\]

Your MCP must be deployed and accessible via HTTPS:

1\. \*\*Endpoint\*\*: Public HTTPS URL (e.g., \`https://your-mcp.example.com\`)  
2\. \*\*Authentication\*\*: Proper authentication mechanism enabled  
3\. \*\*Environment\*\*: Production-ready with proper error handling

Testing Your MCP \[\#testing-your-mcp\]

Before registering with ArmorIQ:

1\. Test the \`/mcp\` endpoint responds to POST requests  
2\. Verify SSE format in responses  
3\. Ensure all three methods (\`initialize\`, \`tools/list\`, \`tools/call\`) work  
4\. Check that tool responses are properly JSON-stringified

Common Issues \[\#common-issues\]

Response Not Streaming \[\#response-not-streaming\]

Ensure you're returning \`StreamingResponse\` with \`media\_type="text/event-stream"\`.

Tools Not Found \[\#tools-not-found\]

Verify your \`tools/list\` response matches the exact format shown above.

Invalid JSON in Response \[\#invalid-json-in-response\]

The \`text\` field in \`tools/call\` response must contain a JSON string, not a raw object.

\# Error Handling

Error Handling \[\#error-handling\]

Exception Hierarchy \[\#exception-hierarchy\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`  
    ArmorIQError (base)  
    ├── AuthenticationError  
    │   ├── InvalidAPIKeyError  
    │   └── APIKeyExpiredError  
    ├── TokenError  
    │   ├── TokenExpiredError  
    │   ├── TokenInvalidError  
    │   └── TokenIssuanceError  
    ├── VerificationError  
    │   ├── MerkleProofError  
    │   └── SignatureError  
    ├── MCPError  
    │   ├── MCPNotFoundError  
    │   ├── ActionNotFoundError  
    │   └── InvalidParametersError  
    ├── NetworkError  
    │   ├── ConnectionError  
    │   └── TimeoutError  
    └── ValidationError  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`  
    ArmorIQException (base)  
    ├── ConfigurationException  
    ├── InvalidTokenException  
    │   └── TokenExpiredException  
    ├── IntentMismatchException  
    ├── MCPInvocationException  
    └── DelegationException  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Catching Exceptions \[\#catching-exceptions\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    from armoriq\_sdk.exceptions import (  
        ArmorIQError,  
        AuthenticationError,  
        TokenExpiredError,  
        VerificationError,  
        MCPError,  
        NetworkError  
    )

    try:  
        captured\_plan \= client.capture\_plan(  
            llm="gpt-4",  
            prompt="Analyze the data",  
            plan=plan\_dict  \# Optional: provide structure  
        )  
        token\_response \= client.get\_intent\_token(captured\_plan)  
        result \= client.invoke("analytics-mcp", "analyze", token\_response\["token"\], params)

    except AuthenticationError as e:  
        \# API key invalid or expired  
        logger.error(f"Authentication failed: {e}")  
        \# Refresh API key

    except TokenExpiredError as e:  
        \# Token expired, get new one  
        logger.warning(f"Token expired: {e}")  
        token\_response \= client.get\_intent\_token(capture\_plan)  
        result \= client.invoke("analytics-mcp", "analyze", token\_response\["token"\], params)

    except VerificationError as e:  
        \# Action not in plan or verification failed  
        logger.error(f"Verification failed: {e}")  
        \# Recreate plan with correct actions

    except MCPError as e:  
        \# MCP execution failed  
        logger.error(f"MCP error: {e.message}")  
        \# Handle MCP-specific error

    except NetworkError as e:  
        \# Network issues  
        logger.error(f"Network error: {e}")  
        \# Retry or use fallback

    except ArmorIQError as e:  
        \# Catch-all for any ArmorIQ error  
        logger.error(f"ArmorIQ error: {e}")

    except Exception as e:  
        \# Unexpected error  
        logger.exception(f"Unexpected error: {e}")  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import {  
      ArmorIQException,  
      ConfigurationException,  
      InvalidTokenException,  
      TokenExpiredException,  
      IntentMismatchException,  
      MCPInvocationException,  
      DelegationException  
    } from '@armoriq/sdk';

    try {  
      const capturedPlan \= client.capturePlan(  
        'gpt-4',  
        'Analyze the data',  
        planDict  // Optional: provide structure  
      );  
      const token \= await client.getIntentToken(capturedPlan);  
      const result \= await client.invoke('analytics-mcp', 'analyze', token, params);

    } catch (error) {  
      if (error instanceof ConfigurationException) {  
        // API key invalid or missing  
        console.error(\`Configuration error: ${error.message}\`);  
        // Check API key format

      } else if (error instanceof TokenExpiredException) {  
        // Token expired, get new one  
        console.warn(\`Token expired: ${error.message}\`);  
        const newToken \= await client.getIntentToken(capturedPlan);  
        const result \= await client.invoke('analytics-mcp', 'analyze', newToken, params);

      } else if (error instanceof IntentMismatchException) {  
        // Action not in plan or verification failed  
        console.error(\`Intent mismatch: ${error.message}\`);  
        console.error(\`Action: ${error.action}, Plan hash: ${error.planHash}\`);  
        // Recreate plan with correct actions

      } else if (error instanceof MCPInvocationException) {  
        // MCP execution failed  
        console.error(\`MCP error: ${error.message}\`);  
        console.error(\`MCP: ${error.mcp}, Action: ${error.action}\`);  
        // Handle MCP-specific error

      } else if (error instanceof InvalidTokenException) {  
        // Token invalid  
        console.error(\`Token error: ${error.message}\`);

      } else if (error instanceof ArmorIQException) {  
        // Catch-all for any ArmorIQ error  
        console.error(\`ArmorIQ error: ${error.message}\`);

      } else {  
        // Unexpected error  
        console.error(\`Unexpected error: ${error}\`);  
      }  
    }  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

Error Response Format \[\#error-response-format\]

When \`invoke()\` returns \`success: False\`:

\`\`\`json  
{  
  "success": false,  
  "error": "str",  
  "error\_code": "str",  
  "details": {},  
  "mcp": "str",  
  "action": "str"  
}  
\`\`\`

Error Codes \[\#error-codes\]

\* \`AUTH\_INVALID\_KEY\`: Invalid API key  
\* \`AUTH\_EXPIRED\_KEY\`: API key expired  
\* \`TOKEN\_EXPIRED\`: Token expired  
\* \`TOKEN\_INVALID\`: Token signature invalid  
\* \`VERIFICATION\_FAILED\`: IAP verification failed  
\* \`MERKLE\_PROOF\_INVALID\`: Merkle proof validation failed  
\* \`MCP\_NOT\_FOUND\`: MCP server not found  
\* \`ACTION\_NOT\_FOUND\`: Action not available  
\* \`INVALID\_PARAMS\`: Invalid parameters  
\* \`NETWORK\_ERROR\`: Network connection failed  
\* \`TIMEOUT\`: Request timed out  
\* \`RATE\_LIMIT\`: Rate limit exceeded

\# Advanced Usage

Advanced Usage \[\#advanced-usage\]

Each advanced topic has its own page. Use the links below to jump directly to the topic you need.

Topics \[\#topics\]

\* \[Custom Retry Logic\](/docs/advanced-usage/custom-retry-logic)  
\* \[Connection Pooling\](/docs/advanced-usage/connection-pooling)  
\* \[Token Caching\](/docs/advanced-usage/token-caching)  
\* \[Batch Invocation\](/docs/advanced-usage/batch-invocation)

\# Connection Pooling

Connection Pooling \[\#connection-pooling\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    from armoriq\_sdk import ArmorIQClient  
    import threading

    class ArmorIQClientPool:  
        def \_\_init\_\_(self, api\_key, user\_id, agent\_id, pool\_size=5):  
            self.pool \= \[  
                ArmorIQClient(api\_key=api\_key, user\_id=user\_id, agent\_id=agent\_id)  
                for \_ in range(pool\_size)  
            \]  
            self.lock \= threading.Lock()  
            self.available \= list(self.pool)

        def get\_client(self):  
            with self.lock:  
                if self.available:  
                    return self.available.pop()  
                \# Pool exhausted, create new client  
                return ArmorIQClient(...)

        def return\_client(self, client):  
            with self.lock:  
                self.available.append(client)

    \# Usage  
    pool \= ArmorIQClientPool(api\_key="...", user\_id="...", agent\_id="...", pool\_size=10)

    def process\_task(task):  
        client \= pool.get\_client()  
        try:  
            \# Use client  
            result \= client.invoke(...)  
            return result  
        finally:  
            pool.return\_client(client)  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import { ArmorIQClient } from '@armoriq/sdk';

    class ArmorIQClientPool {  
      private pool: ArmorIQClient\[\] \= \[\];  
      private available: ArmorIQClient\[\] \= \[\];  
      private apiKey: string;  
      private userId: string;  
      private agentId: string;

      constructor(apiKey: string, userId: string, agentId: string, poolSize: number \= 5\) {  
        this.apiKey \= apiKey;  
        this.userId \= userId;  
        this.agentId \= agentId;  
          
        for (let i \= 0; i \< poolSize; i++) {  
          const client \= new ArmorIQClient({ apiKey, userId, agentId });  
          this.pool.push(client);  
          this.available.push(client);  
        }  
      }

      getClient(): ArmorIQClient {  
        if (this.available.length \> 0\) {  
          return this.available.pop()\!;  
        }  
        // Pool exhausted, create new client  
        return new ArmorIQClient({  
          apiKey: this.apiKey,  
          userId: this.userId,  
          agentId: this.agentId  
        });  
      }

      returnClient(client: ArmorIQClient): void {  
        this.available.push(client);  
      }

      closeAll(): void {  
        this.pool.forEach(client \=\> client.close());  
        this.pool \= \[\];  
        this.available \= \[\];  
      }  
    }

    // Usage  
    const pool \= new ArmorIQClientPool(  
      process.env.ARMORIQ\_API\_KEY\!,  
      process.env.USER\_ID\!,  
      process.env.AGENT\_ID\!,  
      10  
    );

    async function processTask(task: any) {  
      const client \= pool.getClient();  
      try {  
        // Use client  
        const result \= await client.invoke('mcp', 'action', token, {});  
        return result;  
      } finally {  
        pool.returnClient(client);  
      }  
    }  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

\# Token Caching

Token Caching \[\#token-caching\]

Implement token caching to avoid redundant token requests. Cache tokens by plan hash and reuse them until they're close to expiration.

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    import time  
    from typing import Dict, Tuple

    class TokenCache:  
        def \_\_init\_\_(self):  
            self.cache: Dict\[str, Tuple\[str, int\]\] \= {}

        def get(self, plan\_hash: str) \-\> str | None:  
            if plan\_hash in self.cache:  
                token, expires\_at \= self.cache\[plan\_hash\]  
                \# Return token if valid for at least 60 more seconds  
                if time.time() \< expires\_at \- 60:  
                    return token  
            return None

        def set(self, plan\_hash: str, token: str, expires\_at: int):  
            self.cache\[plan\_hash\] \= (token, expires\_at)

        def clear\_expired(self):  
            now \= time.time()  
            self.cache \= {  
                k: v for k, v in self.cache.items()  
                if v\[1\] \> now  
            }

    \# Usage  
    token\_cache \= TokenCache()

    def get\_token\_cached(client, llm, prompt):  
        captured \= client.capture\_plan(llm=llm, prompt=prompt)  
        plan\_hash \= captured.plan\_hash

        \# Try cache first  
        token \= token\_cache.get(plan\_hash)  
        if token:  
            return token

        \# Get new token  
        response \= client.get\_intent\_token(captured)  
        token\_cache.set(plan\_hash, response\["token"\], response\["expires\_at"\])

        return response\["token"\]  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import { IntentToken, ArmorIQClient, PlanCapture } from '@armoriq/sdk';

    class TokenCache {  
      private cache: Map\<string, IntentToken\> \= new Map();

      get(planHash: string): IntentToken | undefined {  
        const token \= this.cache.get(planHash);  
        if (token) {  
          // Return token if valid for at least 60 more seconds  
          if (IntentToken.timeUntilExpiry(token) \> 60\) {  
            return token;  
          }  
          // Token expired or expiring soon, remove from cache  
          this.cache.delete(planHash);  
        }  
        return undefined;  
      }

      set(planHash: string, token: IntentToken): void {  
        this.cache.set(planHash, token);  
      }

      clearExpired(): void {  
        for (const \[hash, token\] of this.cache.entries()) {  
          if (IntentToken.isExpired(token)) {  
            this.cache.delete(hash);  
          }  
        }  
      }  
    }

    // Usage  
    const tokenCache \= new TokenCache();

    async function getTokenCached(  
      client: ArmorIQClient,  
      llm: string,  
      prompt: string,  
      plan: Record\<string, any\>  
    ): Promise\<IntentToken\> {  
      const captured \= client.capturePlan(llm, prompt, plan);  
      const planHash \= captured.plan?.hash || JSON.stringify(captured.plan);

      // Try cache first  
      const cachedToken \= tokenCache.get(planHash);  
      if (cachedToken) {  
        console.log('Using cached token');  
        return cachedToken;  
      }

      // Get new token  
      const token \= await client.getIntentToken(captured);  
      tokenCache.set(planHash, token);

      return token;  
    }  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

\# Batch Invocation

Batch Invocation \[\#batch-invocation\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    import concurrent.futures

    def batch\_invoke(client, mcp, action, token, params\_list, max\_workers=10):  
        """  
        Invoke same action with multiple parameter sets in parallel.

        Args:  
            client: ArmorIQClient instance  
            mcp: MCP name  
            action: Action name  
            token: Intent token  
            params\_list: List of parameter dicts  
            max\_workers: Max concurrent workers

        Returns:  
            List of results in same order as params\_list  
        """  
        def invoke\_one(params):  
            try:  
                return client.invoke(mcp, action, token, params)  
            except Exception as e:  
                return {"success": False, "error": str(e)}

        with concurrent.futures.ThreadPoolExecutor(max\_workers=max\_workers) as executor:  
            futures \= \[executor.submit(invoke\_one, params) for params in params\_list\]  
            return \[f.result() for f in futures\]

    \# Usage  
    captured\_plan \= client.capture\_plan(  
        llm="gpt-4",  
        prompt="Analyze multiple datasets in parallel"  
    )  
    token \= client.get\_intent\_token(captured\_plan)\["token"\]

    params\_list \= \[  
        {"data": \[1, 2, 3\], "metrics": \["mean"\]},  
        {"data": \[4, 5, 6\], "metrics": \["median"\]},  
        {"data": \[7, 8, 9\], "metrics": \["std"\]},  
        \# ... 100 total  
    \]

    results \= batch\_invoke(client, "analytics-mcp", "analyze", token, params\_list)  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import { ArmorIQClient, IntentToken, MCPInvocationResult } from '@armoriq/sdk';

    /\*\*  
     \* Invoke same action with multiple parameter sets in parallel.  
     \*/  
    async function batchInvoke(  
      client: ArmorIQClient,  
      mcp: string,  
      action: string,  
      token: IntentToken,  
      paramsList: Array\<Record\<string, any\>\>,  
      maxConcurrent: number \= 10  
    ): Promise\<Array\<MCPInvocationResult | { success: false; error: string }\>\> {  
      // Process in batches to respect maxConcurrent  
      const results: Array\<MCPInvocationResult | { success: false; error: string }\> \= \[\];  
        
      for (let i \= 0; i \< paramsList.length; i \+= maxConcurrent) {  
        const batch \= paramsList.slice(i, i \+ maxConcurrent);  
        const batchPromises \= batch.map(async (params) \=\> {  
          try {  
            return await client.invoke(mcp, action, token, params);  
          } catch (error: any) {  
            return { success: false as const, error: error.message };  
          }  
        });  
          
        const batchResults \= await Promise.all(batchPromises);  
        results.push(...batchResults);  
      }  
        
      return results;  
    }

    // Usage  
    const plan \= {  
      goal: 'Analyze multiple datasets in parallel',  
      steps: \[  
        { action: 'analyze', mcp: 'analytics-mcp' }  
      \]  
    };

    const capturedPlan \= client.capturePlan(  
      'gpt-4',  
      'Analyze multiple datasets in parallel',  
      plan  
    );  
    const token \= await client.getIntentToken(capturedPlan);

    const paramsList \= \[  
      { data: \[1, 2, 3\], metrics: \['mean'\] },  
      { data: \[4, 5, 6\], metrics: \['median'\] },  
      { data: \[7, 8, 9\], metrics: \['std'\] },  
      // ... 100 total  
    \];

    const results \= await batchInvoke(client, 'analytics-mcp', 'analyze', token, paramsList);  
    console.log(\`Processed ${results.length} invocations\`);  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

\# Configuration

Configuration \[\#configuration\]

Environment Variables \[\#environment-variables\]

\`\`\`bash  
\# Required  
export ARMORIQ\_API\_KEY="ak\_live\_\<64\_hex\_chars\>"  
export ARMORIQ\_USER\_ID="user\_12345"  
export ARMORIQ\_AGENT\_ID="my\_agent\_v1"

\# Optional  
export ARMORIQ\_PROXY\_URL="https://customer-proxy.armoriq.ai"  
export ARMORIQ\_TIMEOUT="30"  
export ARMORIQ\_MAX\_RETRIES="3"  
export ARMORIQ\_VERIFY\_SSL="true"  
export ARMORIQ\_LOG\_LEVEL="INFO"  
\`\`\`

Configuration File \[\#configuration-file\]

Create \`armoriq.yaml\`:

\`\`\`yaml  
api\_key: ${ARMORIQ\_API\_KEY}  
user\_id: user\_12345  
agent\_id: my\_agent\_v1

proxy:  
  url: https://customer-proxy.armoriq.ai  
  timeout: 30  
  max\_retries: 3  
  verify\_ssl: true

logging:  
  level: INFO  
  format: json  
  file: armoriq.log  
\`\`\`

Load configuration:

\`\`\`python  
import yaml  
from armoriq\_sdk import ArmorIQClient

with open("armoriq.yaml") as f:  
    config \= yaml.safe\_load(f)

client \= ArmorIQClient(  
    api\_key=config\["api\_key"\],  
    user\_id=config\["user\_id"\],  
    agent\_id=config\["agent\_id"\],  
    proxy\_url=config\["proxy"\]\["url"\],  
    timeout=config\["proxy"\]\["timeout"\],  
    max\_retries=config\["proxy"\]\["max\_retries"\]  
)  
\`\`\`

Logging Configuration \[\#logging-configuration\]

\`\`\`python  
import logging

\# Configure SDK logging  
logging.basicConfig(  
    level=logging.INFO,  
    format='%(asctime)s \- %(name)s \- %(levelname)s \- %(message)s'  
)

\# Get SDK logger  
logger \= logging.getLogger("armoriq\_sdk")  
logger.setLevel(logging.DEBUG)

\# Add file handler  
handler \= logging.FileHandler("armoriq.log")  
handler.setFormatter(logging.Formatter(  
    '%(asctime)s \- %(name)s \- %(levelname)s \- %(message)s'  
))  
logger.addHandler(handler)

\# Now SDK operations will be logged  
client \= ArmorIQClient(...)  
\`\`\`

\# Troubleshooting

Troubleshooting \[\#troubleshooting\]

Each topic has its own page. Use the links below to jump directly to what you need.

Topics \[\#topics\]

\* \[Debug Mode\](/docs/troubleshooting/debug-mode)  
\* \[Invalid API key format\](/docs/troubleshooting/invalid-api-key-format)  
\* \[Step verification failed\](/docs/troubleshooting/step-verification-failed)  
\* \[Connection refused\](/docs/troubleshooting/connection-refused)  
\* \[Token expired\](/docs/troubleshooting/token-expired)  
\* \[Performance profiling\](/docs/troubleshooting/performance-profiling)

\# Debug Mode

Debug Mode \[\#debug-mode\]

Enable debug mode for detailed logging:

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    import logging  
    logging.basicConfig(level=logging.DEBUG)

    from armoriq\_sdk import ArmorIQClient

    client \= ArmorIQClient(...)  
    client.debug \= True  \# Enable debug mode

    \# Now you'll see detailed request/response logs  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import { ArmorIQClient } from '@armoriq/sdk';

    // Set DEBUG environment variable for detailed logging  
    process.env.DEBUG \= 'armoriq:\*';

    const client \= new ArmorIQClient({  
      apiKey: process.env.ARMORIQ\_API\_KEY\!,  
      userId: 'demo-user',  
      agentId: 'demo-agent'  
    });

    // The SDK automatically logs initialization info  
    // ArmorIQ SDK initialized: mode=production, user=demo-user, agent=demo-agent...

    // You can also check token status  
    import { IntentToken } from '@armoriq/sdk';

    const token \= await client.getIntentToken(planCapture);  
    console.log(\`Token ID: ${token.tokenId}\`);  
    console.log(\`Expires in: ${IntentToken.timeUntilExpiry(token).toFixed(1)}s\`);  
    console.log(\`Plan hash: ${token.planHash.slice(0, 16)}...\`);  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

\# Invalid API key format

Invalid API key format \[\#invalid-api-key-format\]

Cause: API key doesn't match expected format.

Solution:

\`\`\`python  
import os

api\_key \= os.getenv("ARMORIQ\_API\_KEY")

\# Validate format  
assert api\_key.startswith("ak\_live\_"), "API key must start with ak\_live\_"  
assert len(api\_key) \== 72, f"API key must be 72 chars, got {len(api\_key)}"  
assert all(c in "0123456789abcdef" for c in api\_key\[8:\]), "API key must be hex"  
\`\`\`

\# Step verification failed

Step verification failed \[\#step-verification-failed\]

Cause: Action not in original plan or Merkle proof invalid.

Solution:

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# Ensure action is in the plan generated by LLM  
    captured \= client.capture\_plan(  
        llm="gpt-4",  
        prompt="Fetch data and analyze it"  \# LLM will include both actions  
    )  
    token \= client.get\_intent\_token(captured)\["token"\]

    \# This will work \- action matches plan  
    result \= client.invoke("data-mcp", "fetch\_data", token, {})

    \# This will fail \- action not in plan  
    result \= client.invoke("data-mcp", "delete\_data", token, {})  \# ✗  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import { ArmorIQClient, IntentMismatchException } from '@armoriq/sdk';

    // Ensure action is in the plan you provide  
    const plan \= {  
      goal: 'Fetch data and analyze it',  
      steps: \[  
        { action: 'fetch\_data', mcp: 'data-mcp' },  
        { action: 'analyze', mcp: 'analytics-mcp' }  
      \]  
    };

    const captured \= client.capturePlan('gpt-4', 'Fetch data and analyze it', plan);  
    const token \= await client.getIntentToken(captured);

    // This will work \- action matches plan  
    const result \= await client.invoke('data-mcp', 'fetch\_data', token, {});

    // This will fail \- action not in plan  
    try {  
      await client.invoke('data-mcp', 'delete\_data', token, {});  // ✗  
    } catch (error) {  
      if (error instanceof IntentMismatchException) {  
        console.error(\`Action not in plan: ${error.action}\`);  
        console.error('You can only invoke actions that were in the original plan.');  
      }  
    }  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

\# Connection refused

Connection refused \[\#connection-refused\]

Cause: ArmorIQ Proxy not reachable.

Solution:

\`\`\`python  
\# Test connectivity  
import requests

proxy\_url \= "https://customer-proxy.armoriq.ai"

try:  
    response \= requests.get(f"{proxy\_url}/health", timeout=5)  
    if response.status\_code \== 200:  
        print("Proxy reachable")  
    else:  
        print(f"Proxy returned {response.status\_code}")  
except requests.exceptions.ConnectionError:  
    print("Cannot connect to proxy \- check URL and network")  
except requests.exceptions.Timeout:  
    print("Connection timed out \- check firewall")  
\`\`\`

\# Connection refused

Connection refused \[\#connection-refused\]

Cause: ArmorIQ Proxy not reachable.

Solution:

\`\`\`python  
\# Test connectivity  
import requests

proxy\_url \= "https://customer-proxy.armoriq.ai"

try:  
    response \= requests.get(f"{proxy\_url}/health", timeout=5)  
    if response.status\_code \== 200:  
        print("Proxy reachable")  
    else:  
        print(f"Proxy returned {response.status\_code}")  
except requests.exceptions.ConnectionError:  
    print("Cannot connect to proxy \- check URL and network")  
except requests.exceptions.Timeout:  
    print("Connection timed out \- check firewall")  
\`\`\`

\# Performance profiling

Performance profiling \[\#performance-profiling\]

\`\`\`python  
import time  
from contextlib import contextmanager

@contextmanager  
def profile(operation\_name):  
    start \= time.time()  
    try:  
        yield  
    finally:  
        duration \= time.time() \- start  
        print(f"{operation\_name}: {duration:.3f}s")

\# Profile operations  
with profile("capture\_plan"):  
    captured \= client.capture\_plan(llm="gpt-4", prompt="Analyze data")

with profile("get\_token"):  
    token\_response \= client.get\_intent\_token(captured)

with profile("invoke"):  
    result \= client.invoke("analytics-mcp", "analyze", token, params)  
\`\`\`

\# Best Practices

Best Practices \[\#best-practices\]

Each best practice has its own page. Use the links below to jump directly to the topic you need.

Topics \[\#topics\]

\* \[Client Lifecycle Management\](/docs/best-practices/client-lifecycle-management)  
\* \[Error Recovery\](/docs/best-practices/error-recovery)  
\* \[Monitoring and Metrics\](/docs/best-practices/monitoring-and-metrics)  
\* \[Testing\](/docs/best-practices/testing)

\# Error Recovery

Error Recovery \[\#error-recovery\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    \# ✓ Good \- Graceful degradation  
    def invoke\_with\_fallback(client, mcp, action, token, params, fallback\_value=None):  
        try:  
            result \= client.invoke(mcp, action, token, params)  
            if result\["success"\]:  
                return result\["data"\]  
            else:  
                logger.warning(f"MCP failed: {result\['error'\]}")  
                return fallback\_value  
        except Exception as e:  
            logger.error(f"Invoke failed: {e}")  
            return fallback\_value

    \# Usage  
    data \= invoke\_with\_fallback(  
        client, "data-mcp", "fetch", token, {},  
        fallback\_value=\[\]  \# Empty list if fails  
    )  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import { ArmorIQClient, IntentToken, MCPInvocationException } from '@armoriq/sdk';

    // ✓ Good \- Graceful degradation  
    async function invokeWithFallback\<T\>(  
      client: ArmorIQClient,  
      mcp: string,  
      action: string,  
      token: IntentToken,  
      params: Record\<string, any\>,  
      fallbackValue: T  
    ): Promise\<T\> {  
      try {  
        const result \= await client.invoke(mcp, action, token, params);  
        return result.result as T;  
      } catch (error) {  
        if (error instanceof MCPInvocationException) {  
          console.warn(\`MCP failed: ${error.message}\`);  
        } else {  
          console.error(\`Invoke failed: ${error}\`);  
        }  
        return fallbackValue;  
      }  
    }

    // Usage  
    const data \= await invokeWithFallback(  
      client,  
      'data-mcp',  
      'fetch',  
      token,  
      {},  
      \[\]  // Empty array if fails  
    );  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

\# Monitoring and Metrics

Monitoring and Metrics \[\#monitoring-and-metrics\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    import time  
    from dataclasses import dataclass  
    from typing import List

    @dataclass  
    class InvokeMetric:  
        mcp: str  
        action: str  
        success: bool  
        duration\_ms: float  
        timestamp: float

    class MetricsCollector:  
        def \_\_init\_\_(self):  
            self.metrics: List\[InvokeMetric\] \= \[\]

        def record(self, mcp, action, success, duration\_ms):  
            self.metrics.append(InvokeMetric(  
                mcp=mcp,  
                action=action,  
                success=success,  
                duration\_ms=duration\_ms,  
                timestamp=time.time()  
            ))

        def get\_stats(self):  
            if not self.metrics:  
                return {}

            total \= len(self.metrics)  
            successful \= sum(1 for m in self.metrics if m.success)  
            avg\_duration \= sum(m.duration\_ms for m in self.metrics) / total

            return {  
                "total\_invocations": total,  
                "successful": successful,  
                "failed": total \- successful,  
                "success\_rate": successful / total,  
                "avg\_duration\_ms": avg\_duration  
            }

    \# Usage  
    metrics \= MetricsCollector()

    start \= time.time()  
    result \= client.invoke(mcp, action, token, params)  
    duration\_ms \= (time.time() \- start) \* 1000

    metrics.record(mcp, action, result\["success"\], duration\_ms)

    \# Later  
    print(metrics.get\_stats())  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    interface InvokeMetric {  
      mcp: string;  
      action: string;  
      success: boolean;  
      durationMs: number;  
      timestamp: number;  
    }

    class MetricsCollector {  
      private metrics: InvokeMetric\[\] \= \[\];

      record(mcp: string, action: string, success: boolean, durationMs: number): void {  
        this.metrics.push({  
          mcp,  
          action,  
          success,  
          durationMs,  
          timestamp: Date.now()  
        });  
      }

      getStats(): Record\<string, any\> {  
        if (this.metrics.length \=== 0\) {  
          return {};  
        }

        const total \= this.metrics.length;  
        const successful \= this.metrics.filter(m \=\> m.success).length;  
        const avgDuration \= this.metrics.reduce((sum, m) \=\> sum \+ m.durationMs, 0\) / total;

        return {  
          totalInvocations: total,  
          successful,  
          failed: total \- successful,  
          successRate: successful / total,  
          avgDurationMs: avgDuration  
        };  
      }  
    }

    // Usage  
    const metrics \= new MetricsCollector();

    const start \= Date.now();  
    const result \= await client.invoke(mcp, action, token, params);  
    const durationMs \= Date.now() \- start;

    metrics.record(mcp, action, result.status \=== 'success', durationMs);

    // Later  
    console.log(metrics.getStats());  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

\# Testing

Testing \[\#testing\]

\<Tabs groupId="language" items={\['Python', 'TypeScript'\]}\>  
  \<Tab value="Python"\>  
    \`\`\`python  
    import unittest  
    from unittest.mock import patch

    class TestAgent(unittest.TestCase):  
        def setUp(self):  
            self.client \= ArmorIQClient(  
                api\_key="ak\_live\_" \+ "a" \* 64,  
                user\_id="test\_user",  
                agent\_id="test\_agent"  
            )

        @patch('armoriq\_sdk.client.ArmorIQClient.invoke')  
        def test\_successful\_invocation(self, mock\_invoke):  
            \# Mock successful response  
            mock\_invoke.return\_value \= {  
                "success": True,  
                "data": {"result": 42},  
                "execution\_time\_ms": 100  
            }

            result \= self.client.invoke("math-mcp", "calculate", "token", {})

            self.assertTrue(result\["success"\])  
            self.assertEqual(result\["data"\]\["result"\], 42\)

        @patch('armoriq\_sdk.client.ArmorIQClient.get\_intent\_token')  
        def test\_token\_expiration\_handling(self, mock\_get\_token):  
            \# First call returns expired token  
            \# Second call returns fresh token  
            mock\_get\_token.side\_effect \= \[  
                {"token": "expired\_token", "expires\_at": 0},  
                {"token": "fresh\_token", "expires\_at": 9999999999}  
            \]

            \# Test auto-refresh logic  
            ...  
    \`\`\`  
  \</Tab\>

  \<Tab value="TypeScript"\>  
    \`\`\`typescript  
    import { ArmorIQClient, IntentToken, MCPInvocationResult } from '@armoriq/sdk';  
    import { jest, describe, it, expect, beforeEach } from '@jest/globals';

    describe('ArmorIQ Agent Tests', () \=\> {  
      let client: ArmorIQClient;

      beforeEach(() \=\> {  
        // Mock environment variables  
        process.env.ARMORIQ\_API\_KEY \= 'ak\_test\_' \+ 'a'.repeat(64);  
        process.env.USER\_ID \= 'test\_user';  
        process.env.AGENT\_ID \= 'test\_agent';

        client \= new ArmorIQClient({  
          apiKey: process.env.ARMORIQ\_API\_KEY,  
          userId: process.env.USER\_ID,  
          agentId: process.env.AGENT\_ID,  
          useProduction: false  
        });  
      });

      it('should successfully invoke an action', async () \=\> {  
        // Mock the invoke method  
        const mockResult: MCPInvocationResult \= {  
          mcp: 'math-mcp',  
          action: 'calculate',  
          result: { value: 42 },  
          status: 'success',  
          executionTime: 0.1,  
          verified: true,  
          metadata: {}  
        };

        jest.spyOn(client, 'invoke').mockResolvedValue(mockResult);

        const result \= await client.invoke(  
          'math-mcp',  
          'calculate',  
          {} as IntentToken,  
          {}  
        );

        expect(result.status).toBe('success');  
        expect(result.result.value).toBe(42);  
      });

      it('should handle token expiration', async () \=\> {  
        const mockToken: Partial\<IntentToken\> \= {  
          tokenId: 'test-token',  
          expiresAt: Date.now() / 1000 \+ 3600  // 1 hour from now  
        };

        jest.spyOn(client, 'getIntentToken').mockResolvedValue(mockToken as IntentToken);

        const token \= await client.getIntentToken({} as any);  
          
        expect(IntentToken.isExpired(token as IntentToken)).toBe(false);  
        expect(IntentToken.timeUntilExpiry(token as IntentToken)).toBeGreaterThan(3500);  
      });  
    });  
    \`\`\`  
  \</Tab\>  
\</Tabs\>

