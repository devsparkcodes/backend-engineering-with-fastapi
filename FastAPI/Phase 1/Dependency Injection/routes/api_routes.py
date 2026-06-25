from fastapi import APIRouter, HTTPException, Depends

from models import StudentCreate, StudentResponse
from services import student_service
from database import get_db

router = APIRouter(
    prefix="/students",
)

@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate, db=Depends(get_db)):
    data = student.model_dump()

    return student_service.create_student(db, data)

@router.get("/", response_model=list[StudentResponse])
def get_all_students(db=Depends(get_db)):

    return student_service.get_all_students(db)

@router.get("/{student_id}", response_model=StudentResponse)
def get_by_id(student_id: int, db=Depends(get_db)):
    student = student_service.get_by_id(student_id, db)
    if not student:
        raise HTTPException(
            status_code=404,
            detail=f"Student with {student_id} not found."
        )
    
    return student

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
        student_id: int, 
        updated_data: StudentCreate, 
        db=Depends(get_db)
    ):
    data = updated_data.model_dump()
    
    return student_service.update_student(student_id, data, db)

@router.delete("/{student_id}")
def delete_student(student_id: int, db=Depends(get_db)):
    student = student_service.delete_student(student_id, db)
    if not student:
        raise HTTPException(
            status_code=404,
            detail=f"Student with {student_id} not found."
        )
    
    return {
        "message": f"Student with {student_id} id deleted!",
        "student": student
    }