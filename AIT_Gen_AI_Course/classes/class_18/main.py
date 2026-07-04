# from typing import TypedDict

# class ChatResponse(TypedDict):
#     intent: str
#     confidence: float
#     answer: str
#     follow_up_questions: list[str]
    
# response = ChatResponse(
#     intent="product_inquiry",
#     confidence=0.92,
#     answer="The Y80 Ultra smartwatch is available for $199.",
#     follow_up_questions=[
#         "Would you like to know about shipping options?",
#         "Do you want me to compare it with other smartwatches?"
#     ]
# )

# print(response)


from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated
import os

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")    
)

class ChatResponse(TypedDict):
    intent: Annotated[str, "The detected user intent (e.g., 'product_inquiry', 'order_status', 'greeting')"]
    
    confidence: Annotated[float, "A confidence score between 0  and 1 representing how sure the model is about the intent"]
    
    answer: Annotated[str, "The chatbot's primary response to the user query"]
    
    follow_up_questions: Annotated[list[str], "Suggested follow-up questions to keep the conversation flowing (can be empty)"]
    
structured_model = model.with_structured_output(ChatResponse)

result = structured_model.invoke(
    """
    Hi, there! I ordered  a smartwatch last week, but i haven't received any update yet.
    Can you tell me the status of my order?
    """
)

for res in result.items():
    print(res)

# print(result)