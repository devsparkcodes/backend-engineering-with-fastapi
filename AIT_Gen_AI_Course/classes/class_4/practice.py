from fastapi import FastAPI

app = FastAPI()

students = []

@app.post("/students")
def std_data(student: dict):
    student["id"] = len(students) + 1
    students.append(student)
    return {
        "status": "Student registered!",
        "student": students
    }
