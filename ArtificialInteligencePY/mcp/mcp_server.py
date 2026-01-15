from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Simple MCP Server")

# ===== MCP Schemas =====

class ToolDescription(BaseModel):
    name: str
    description: str
    input_schema: Dict
    output_schema: Dict


class AddInput(BaseModel):
    a: float
    b: float


class AddOutput(BaseModel):
    result: float


TOOLS = {
    "add": ToolDescription(
        name="add",
        description="Soma dois números",
        input_schema={"a": "number", "b": "number"},
        output_schema={"result": "number"},
    )
}


# ===== MCP Endpoints =====

@app.get("/mcp/tools")
def list_tools():
    return TOOLS


@app.post("/mcp/invoke/{tool_name}")
def invoke_tool(tool_name: str, payload: dict):
    if tool_name == "add":
        data = AddInput(**payload)
        return AddOutput(result=data.a + data.b)

    return {"error": f"Tool '{tool_name}' not found"}
