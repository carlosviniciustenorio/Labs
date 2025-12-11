import requests
import json

prompt = "Hey, What's up bro? lemme know how to programming in Python?"

r = requests.post("http://localhost:11434/api/generate", json={
    "model": "mistral",
    "prompt": prompt
}, stream=True)

for chunk in r.iter_lines():
    if chunk:
        print(json.loads(chunk)["response"], end="")