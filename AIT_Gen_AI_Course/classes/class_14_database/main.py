from dotenv import load_dotenv
from groq import Groq
from fastapi import FastAPI
from pydantic import BaseModel
import os

# Load .env into environment
load_dotenv()

# # Create a Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
app = FastAPI()

class Question(BaseModel):
    text: str

# Output schema
class Answer(BaseModel):
    question: str
    answer: str


# chat_history = []

# @app.post("/chat", response_model=Answer)
# def chat(question: Question):
#     # Add this question to history
#     chat_history.append({"role": "user", "content": question.text})

#     # Send the WHOLE history to the LLM
#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=chat_history,
#     )

#     answer_text = response.choices[0].message.content

#     # Save the LLM's answer in history too
#     chat_history.append({"role": "assistant", "content": answer_text})

#     return Answer(question=question.text, answer=answer_text)

# @app.get("/chat/history")
# def get_history():
#     return chat_history

# @app.delete("/chat/history")
# def clear_history():
#     chat_history.clear()
#     return {"message": "History cleared"}


from sqlmodel import SQLModel, Field, Session, create_engine, select
from datetime import datetime

class ChatLog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    question: str
    answer: str
    created_at: datetime = Field(default_factory=datetime.now)

engine = create_engine("sqlite:///chats.db")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post("/ask-and-save", response_model=Answer)
def ask_and_save(question: Question):
    # Call the LLM
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": question.text}],
    )
    answer_text = response.choices[0].message.content

    # Save to the database
    with Session(engine) as session:
        log = ChatLog(question=question.text, answer=answer_text)
        session.add(log)
        session.commit()

    return Answer(question=question.text, answer=answer_text)

@app.get("/chats")
def list_chats():
    with Session(engine) as session:
        return session.exec(select(ChatLog)).all()