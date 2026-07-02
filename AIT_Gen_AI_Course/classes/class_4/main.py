from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/calculator")
def calculator(a: int, b: int, c: str):
    if (c == "+"):
        return {"sum of a and b": a + b}
    elif (c == "-"):
        return {"subtraction of a and b": a - b}
    elif (c == "*"):
        return {"product of a and b": a * b}
    elif (c == "/"):
        return {"division of a and b": a / b}
    else:
        return {"result": "operator not found."}
    

@app.get("/age-in-years")
def calculate_age(birth_year: int):
    current_year = datetime.now().now.year
    age = current_year - birth_year
    return {
        "birth_year": birth_year,
        "current_year": current_year,
        "age": age
    }