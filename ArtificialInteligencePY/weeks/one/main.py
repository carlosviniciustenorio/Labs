from openai import OpenAI
import datetime

client = OpenAI()

def perguntar_gpt(pergunta: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4.1-mini",  # barato e rápido
        messages=[
            {"role": "user", "content": pergunta}
        ]
    )
    return resp.choices[0].message.content


def salvar_resposta(pergunta: str, resposta: str):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("conversas.txt", "a", encoding="utf-8") as f:
        f.write(f"==== {now} ====\n")
        f.write(f"Pergunta: {pergunta}\n")
        f.write(f"Resposta: {resposta}\n\n")


def main():
    print("Digite sua pergunta para o GPT (ou 'sair' para encerrar).")
    while True:
        pergunta = input("> ")
        if pergunta.lower() == "sair":
            break

        resposta = perguntar_gpt(pergunta)
        print("\nGPT:", resposta, "\n")
        salvar_resposta(pergunta, resposta)


if __name__ == "__main__":
    main()