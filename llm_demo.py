
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

# Step 1: Create a reusable prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Explain concepts clearly."),
    ("human", "Explain {topic} in 3 simple sentences.")
])

# Step 2: Connect to the local Qwen model
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

# Step 3: Create an output parser
output_parser = StrOutputParser()

# Step 4: Connect the components into a chain
chain = prompt | llm | output_parser

# Step 5: Execute the chain
response = chain.invoke({
    "topic": "Retrieval-Augmented Generation (RAG)"
})

# Step 6: Display the generated answer
print("\nAI Response:\n")
print(response)