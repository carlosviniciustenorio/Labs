import requests
from langchain_core.tools import tool

BASE_URL = "http://localhost:3333"


def invoke_mcp(tool_name: str, payload: dict):
    url = f"{BASE_URL}/mcp/invoke/{tool_name}"
    resp = requests.post(url, json=payload, timeout=5)
    resp.raise_for_status()
    return resp.json()


@tool
def add_numbers(a: float, b: float) -> str:
    """
    Soma dois números usando um MCP Server externo.
    """
    result = invoke_mcp("add", {"a": a, "b": b})
    return str(result)
