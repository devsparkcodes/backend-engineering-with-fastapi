from pydantic import BaseModel, Field, EmailStr

class StudentBase(BaseModel):

    name: str = Field(
        ...,
        min_length=3,
        max_length=20
    )

    father_name: str = Field(
        ...,
        min_length=3,
        max_length=20
    )

    age: int = Field(
        ...,
        ge=5,
        le=18
    )

    class_name: int = Field(
        ...,
        ge=3,
        le=10
    )

    grade: str = Field(
        ...,
        pattern=r"[A-F][+-]?$"
    )

    parent_email: EmailStr = Field(...)


class StudentCreate(StudentBase):
    password: str = Field(...)


class StudentResponse(StudentBase):
    id: int