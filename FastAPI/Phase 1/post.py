from fastapi import FastAPI, status

app = FastAPI()

@app.post("/studetns", status_code=status.HTTP_201_CREATED)
def create_students(student: dict):
    return {
        "received_data": student
    }