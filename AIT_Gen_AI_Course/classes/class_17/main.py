from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

messages = [
    SystemMessage(content="You are a helpful assistant")
]

while True:
    user_input = input("Enter Prompt: ")
    messages.append(HumanMessage(content=user_input))
    result = llm.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print(f"AI: {result.content}")
    for msg in messages:
        print(msg.content)
    
    
    
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(model="llama-3.3-70b-versatile")
# messages = [
#     SystemMessage(content = 'You Are Helpful Assistant.')
# ]
# while True:
#     user_input = input("You: ")
#     messages.append(HumanMessage(content=user_input))
#     response = llm.invoke(messages)
#     messages.append(AIMessage(content=response.content))
#     print(f"AI: {response.content}\n")
#     print(messages)