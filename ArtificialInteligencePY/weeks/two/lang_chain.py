from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="mistral",
    temperature=3
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um agente chamado ArchAgent, especialista em arquitetura de backend."),
    ("human", "{pergunta}")
])

chain = prompt | llm | StrOutputParser()

resposta = chain.invoke({"pergunta": "What's reverse engineer?"})
print(resposta)