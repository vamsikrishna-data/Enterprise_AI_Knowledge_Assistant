
from langchain_core.prompts import ChatPromptTemplate

# Step 1: Define a reusable prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Explain concepts clearly."),
    ("human", "Explain {topic} in simple terms.")
])

# Step 2: Supply a value for the placeholder
formatted_prompt = prompt.invoke({
    "topic": "Retrieval-Augmented Generation (RAG)"
})

# Step 3: Display the formatted messages
for message in formatted_prompt.messages:
    print(f"{message.type}: {message.content}")
