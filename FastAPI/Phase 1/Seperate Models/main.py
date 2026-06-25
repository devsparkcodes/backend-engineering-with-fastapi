from fastapi import FastAPI
from models import StudentCreate, StudentResponse

app = FastAPI()

db = {}
current_id = 1

@app.post("/studetns", response_model=StudentResponse)
def student_create(student: StudentCreate):
    global current_id

    data = student.model_dump()

    data["id"] = current_id
    db[current_id] = data
    current_id += 1

    return data