from fastapi import FastAPI
from routes.api_routes import router as student_router

app = FastAPI()

app.include_router(student_router)