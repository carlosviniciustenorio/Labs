``` mermaid
sequenceDiagram
    autonumber

    participant User
    participant Agent as LangChain Agent
    participant LLM as Ollama (Mistral)
    participant Tool as LangChain Tool Wrapper
    participant MCPClient as MCP Client
    participant MCPServer as MCP Server
    participant Logic as Tool Logic

    User->>Agent: Input question
    Agent->>LLM: Build prompt + context
    LLM-->>Agent: Decide to call tool

    Agent->>Tool: add_numbers(a,b)
    Tool->>MCPClient: invoke("add", payload)
    MCPClient->>MCPServer: POST /mcp/invoke/add
    MCPServer->>Logic: Execute add(a,b)
    Logic-->>MCPServer: result
    MCPServer-->>MCPClient: { result }
    MCPClient-->>Tool: response
    Tool-->>Agent: Tool output

    Agent->>LLM: Inject tool result
    LLM-->>Agent: Final answer
    Agent-->>User: Response
```