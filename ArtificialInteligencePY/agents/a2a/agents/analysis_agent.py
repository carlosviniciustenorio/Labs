from infra.message_bus import subscribe, publish
from infra.ollama_client import generate


def run():

    for msg in subscribe("analysis"):

        if msg["type"] == "research_result":

            topic = msg["payload"]["topic"]
            data = msg["payload"]["data"]

            prompt = f"""
You are a strategy analyst.

Topic: {topic}

Signals:
{data}

Provide a short strategic insight.
"""

            insight = generate(prompt)

            publish("response", {
                "from": "analysis",
                "to": "response",
                "type": "analysis_result",
                "payload": {
                    "insight": insight
                }
            })