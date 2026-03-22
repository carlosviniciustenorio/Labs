import requests

BASE_URL = "http://localhost:3333"


def list_tools():
    return requests.get(f"{BASE_URL}/mcp/tools").json()


def invoke(tool_name: str, payload: dict):
    return requests.post(f"{BASE_URL}/mcp/invoke/{tool_name}", json=payload).json()


if __name__ == "__main__":
    print("🔹 Ferramentas disponíveis:")
    tools = list_tools()
    for name, meta in tools.items():
        print(f"- {name}: {meta['description']}")

    print("\n🔹 Chamando add(2, 3)...")
    result = invoke("add", {"a": 2, "b": 3})
    print("Resultado:", result)
