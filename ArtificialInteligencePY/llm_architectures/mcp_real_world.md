``` mermaid

flowchart LR
    User[👤 User Prompt]

    subgraph Agent_Runtime["🤖 Agent Runtime (LangChain / LangGraph)"]
        Planner[🧠 LLM + Tool Planner]
        ToolExec[⚙️ Tool Executor]
    end

    subgraph MCP_Client["🔌 MCP Client"]
        Discovery[🔍 Handshake + list_tools]
        Router[🧭 call_tool Router]
    end

    subgraph MCP_Server["🧩 MCP Server"]
        Protocol[📜 MCP Protocol Layer]
        ToolsRegistry[🗂 Tool Registry]
        Executors[🚀 Tool Executors]
    end

    subgraph External_Services["🌍 External World"]
        Outlook[📧 Outlook API]
        DB[(🗄 Database)]
        AWS[☁️ AWS Services]
        HTTP[🌐 Public APIs]
    end

    User --> Planner
    Planner --> ToolExec

    ToolExec --> Discovery
    Discovery --> Planner

    ToolExec --> Router
    Router --> Protocol

    Protocol --> ToolsRegistry
    ToolsRegistry --> Executors

    Executors --> Outlook
    Executors --> DB
    Executors --> AWS
    Executors --> HTTP

    Outlook --> Executors
    DB --> Executors
    AWS --> Executors
    HTTP --> Executors

    Executors --> Protocol
    Protocol --> Router
    Router --> ToolExec
    ToolExec --> Planner
```