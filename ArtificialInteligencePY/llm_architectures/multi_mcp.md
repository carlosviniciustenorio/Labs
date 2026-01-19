``` mermaid
flowchart LR
    Agent[🤖 Agent]

    MCP1[📦 MCP - Email]
    MCP2[📦 MCP - CRM]
    MCP3[📦 MCP - Data]
    MCP4[📦 MCP - Cloud]

    Agent --> MCP1
    Agent --> MCP2
    Agent --> MCP3
    Agent --> MCP4

    MCP1 --> Outlook[📧 Outlook]
    MCP2 --> CRM[🏢 CRM]
    MCP3 --> Lake[(🗄 Data Lake)]
    MCP4 --> AWS[☁️ AWS]
```