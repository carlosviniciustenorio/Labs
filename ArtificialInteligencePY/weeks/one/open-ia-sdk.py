from openai import OpenAI
client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Olá!"}]
)

print(f'Integration Response: {resp.choices[0].message}')