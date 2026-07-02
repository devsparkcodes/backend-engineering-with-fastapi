from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(min_length=1, max_length=15)
    age: int = Field(gt=0, lt=120)
    grade_percentage: float = Field(ge=0, le=100)