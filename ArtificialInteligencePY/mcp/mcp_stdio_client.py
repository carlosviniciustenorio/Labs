import subprocess
import json
import uuid


class MCPClient:
    def __init__(self, command):
        self.proc = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def send(self, payload: dict):
        payload["id"] = payload.get("id", str(uuid.uuid4()))
        self.proc.stdin.write(json.dumps(payload) + "\n")
        self.proc.stdin.flush()

        line = self.proc.stdout.readline()
        return json.loads(line)

    def initialize(self):
        return self.send({"type": "initialize"})

    def list_tools(self):
        return self.send({"type": "list_tools"})

    def call_tool(self, tool, arguments):
        return self.send({
            "type": "call_tool",
            "tool": tool,
            "arguments": arguments
        })


if __name__ == "__main__":
    client = MCPClient(["python3", "mcp_stdio_server.py"])

    print("🔹 Initialize")
    print(client.initialize())

    print("\n🔹 List tools")
    print(client.list_tools())

    print("\n🔹 Call tool add")
    print(client.call_tool("add", {"a": 10, "b": 32}))
