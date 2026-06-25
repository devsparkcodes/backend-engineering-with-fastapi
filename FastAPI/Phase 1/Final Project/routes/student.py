from fastapi import APIRouter, HTTPException

from models import StudentCreate, StudentResponse
from services import student_service
import database

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# Create Student
@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate):
    
    data = student.model_dump()

    return student_service.create_student(data)

# Get All Students
@router.get("/", response_model=list[StudentResponse])
def get_all_students():
    return student_service.get_all_students()

# Get Student by Id
@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(student_id: int):

    student = student_service.get_student(student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail=f"Student with {student_id} id not found!"
        )
    
    return student

# Update Student
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, updated_student: StudentCreate):

    data = updated_student.model_dump()

    student = student_service.update_student(student_id, data)

    if not student:
        raise HTTPException(
            status_code=404,
            detail=f"Student with {student_id} id not found!"
        )

    return student

# Delete Student
@router.delete("/{student_id}")
def delete_student(student_id: int):

    student = student_service.delete_student(student_id)
    
    if not student:
        raise HTTPException(
            status_code=404,
            detail=f"Student with {student_id} id not found!"
        )

    return {
        "message": f"Student with {student_id} id deleted!",
        "student": student
    }