from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langfuse.langchain import CallbackHandler


handler = CallbackHandler()

llm = ChatOllama(
    model="mistral",
    temperature=0.3,
    callbacks=[handler],
)

prompt = ChatPromptTemplate([
    ("system","You're staff solutions architect, please teach about the question."),
    ("human", "{ask}")
])

chain = prompt | llm | StrOutputParser()

while 0 <= 0:
    response = chain.invoke(
        {"ask": "Lemme know about Apache Kafka in just one sentence"},
        config={"callbacks": [handler]}
    )

print(response)