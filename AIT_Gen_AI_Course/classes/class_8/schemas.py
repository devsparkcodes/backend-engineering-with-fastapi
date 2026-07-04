from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    name: str
    father_name: str
    age: int
    email: str
    password: str = Field(min_length=4, max_length=8)

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str