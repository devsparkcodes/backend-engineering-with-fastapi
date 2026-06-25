from fastapi import FastAPI

app = FastAPI()

db = {
    "1": {
        "name": "Muhammad Umar",
        "age": 16,
        "class": 10
    },

    "2": {
        "name": "Muhammad Usman",
        "age": 16,
        "class": 10
    },

    "3": {
        "name": "Hamza",
        "age": 18,
        "class": 12
    },

    "4": {
        "name": "Muhammad Affan",
        "age": 13,
        "class": 8
    }
}

@app.get("/students")
def create_student():
    return list(db.values())