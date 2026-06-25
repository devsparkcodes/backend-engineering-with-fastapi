from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class Student(BaseModel):
    name: str = Field(min_length=3, max_length=15)
    age: int = Field(ge=5, le=16)
    email: EmailStr
    grade: str = Field(
        pattern=r"^[A-F][+-]?$"
    )

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created!",
        "student": student
    }