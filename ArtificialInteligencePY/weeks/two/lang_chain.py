from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

llm = ChatOllama(
    model="mistral",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente técnico."),
    ("human", "{pergunta}")
])

chain = prompt | llm | StrOutputParser()

resposta = chain.invoke({"pergunta": "Explique gRPC em uma frase."})
print(resposta)