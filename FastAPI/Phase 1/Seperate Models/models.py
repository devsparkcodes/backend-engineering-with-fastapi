from pydantic import BaseModel, Field, EmailStr

# BaseClass
class StudentBase(BaseModel):
    name: str = Field(
        min_length=3, max_length=20
    )
    father_name: str = Field(
        min_length=3, max_length=20
    )
    age: int = Field(
        ge=5,
        le=18
    )
    grade: str = Field(
        pattern=r"[A-F][+-]?$"
    )

# CreateClass
class StudentCreate(StudentBase):
    email: EmailStr
    password: str

# ResponseClass
class StudentResponse(StudentBase):
    id: int