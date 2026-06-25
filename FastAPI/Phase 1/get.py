from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Umar!"}

@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }