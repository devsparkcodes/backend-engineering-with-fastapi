from fastapi import FastAPI, HTTPException
from models import StudentCreate, StudentResponse

app = FastAPI()

current_id = 1
db = {}

@app.post("/students")
def create_student(student: StudentCreate):
    global current_id

    data = student.model_dump()
    data["id"] = current_id
    db[current_id] = data

    current_id += 1

    return {
        "message": "Student Created",
        "student_id": data["id"]
    }

@app.get("/students", response_model=list[StudentResponse])
def get_all_students():
    return list(db.values())

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    if student_id in db.keys():
        return db[student_id]
    
    raise HTTPException(status_code=404, detail="Student not found")