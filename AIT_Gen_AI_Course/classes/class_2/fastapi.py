from fastapi import FastAPI

# Create a FastAPI application
app = FastAPI()

# Create an endpoint
@app.get("/")
def hello():
    return {"message": "Hello World!"}