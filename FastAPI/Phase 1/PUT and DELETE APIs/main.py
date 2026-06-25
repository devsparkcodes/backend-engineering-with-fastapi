from fastapi import FastAPI, HTTPException
from models import StudentCreate, StudentResponse

app = FastAPI()

db = {}
current_id = 1

@app.post("/students")
def create_student(student: StudentCreate):
    global current_id

    data = student.model_dump()
    data["id"] = current_id
    db[current_id] = data

    current_id += 1

    return {
        "message": "Student Created!",
        "student_id": data["id"]
    }

@app.get("/students", response_model=list[StudentResponse])
def get_all_students():
    return list(db.values())

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_by_id(student_id: int):
    if student_id not in db.keys():
        raise HTTPException(
            status_code=404,
            detail=f"Student with {student_id} id not found!"
        )
    return db[student_id]

@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, updated_student: StudentCreate):
    if student_id not in db.keys():
        raise HTTPException(
            status_code=404,
            detail=f"Student with {student_id} id not found!"
        )
    
    data = updated_student.model_dump()
    data["id"] = student_id
    db[student_id] = data

    return data

@app.delete("/students{student_id}")
def delete_student(student_id: int):
    if student_id not in db.keys():
        raise HTTPException(
            status_code=404,
            detail=f"Student with {student_id} id not found!"
        )
    
    deleted_student = db.pop(student_id)

    return {
        "message": "Student deleted!",
        "student": deleted_student
    }