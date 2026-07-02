from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
students = []

class Student(BaseModel):
    name: str
    age: int
    class_name: str
    
@app.post("/students")
def add_student(student: Student):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "age": student.age,
        "class_name": student.class_name
    }
    students.append(new_student)
    return new_student