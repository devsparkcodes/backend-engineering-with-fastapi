from fastapi import FastAPI
from schemas import StudentCreate, StudentResponse

app = FastAPI()
students = []

@app.post("/students", response_model=StudentResponse)
def add_student(student: StudentCreate):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "father_name": student.father_name,
        "age": student.age,
        "email": student.email,
        "password": student.password
    }
    students.append(new_student)
    return new_student
