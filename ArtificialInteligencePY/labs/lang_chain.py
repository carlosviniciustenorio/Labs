from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="mistral",
    temperature=5
)

prompt = ChatPromptTemplate.from_messages([
    ("system","you're Staff Agent, like a staff software engineer and should be able to awnser anything about technologies. But only in one hundred caracheteres"),
    ("human","{ask}")
])

chain = prompt | llm | StrOutputParser()

response = chain.invoke({"ask":"What's Kafka and how does it work?"})
print(response)