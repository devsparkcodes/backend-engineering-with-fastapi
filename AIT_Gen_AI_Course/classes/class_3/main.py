from fastapi import FastAPI

# Create a FastAPI application
app = FastAPI()

# Create an endpoint
@app.get("/")
def hello():
    return {"message": "Hello World!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}