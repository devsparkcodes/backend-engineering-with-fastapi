from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Student(BaseModel):

    name: str = Field(    # Field(...) -> name required!
        min_length=2,
        max_length=50
    )

    age: int = Field(
        ge=5,
        le=100
    )

    grade: str

@app.post("/students")
def create_student(student: Student):

    return {
        "message": "Student created",
        "student": student
    }
