``` mermaid
flowchart TD
    User((User Input))

    %% Runtime
    Runtime[Agent Runtime / Orchestrator]

    %% Stages
    Perception[Perception / Intent فهم]
    Planner[Planner Agent]
    Discovery[Tool Discovery]
    Executor[Executor Agent]
    Validator[Validator / Critic Agent]
    Reflect[Reflection]
    Memory[Memory Agent]

    %% Tools
    subgraph Tools["Tools / Capabilities"]
        RAG[RAG / Vector DB]
        MCP[MCP Servers]
        API[External APIs]
        DB[(Databases)]
        Email[Email / Jobs]
    end

    %% Flow
    User --> Runtime
    Runtime --> Perception
    Perception --> Planner
    Planner --> Discovery
    Discovery --> Planner
    Planner --> Executor

    Executor -->|call| RAG
    Executor -->|call| MCP
    Executor -->|call| API
    Executor -->|call| DB
    Executor -->|call| Email

    RAG --> Executor
    MCP --> Executor
    API --> Executor
    DB --> Executor
    Email --> Executor

    Executor --> Validator
    Validator --> Reflect
    Reflect -->|retry| Planner
    Reflect --> Memory
    Memory --> Runtime
    Runtime --> User


```