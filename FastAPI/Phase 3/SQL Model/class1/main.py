from sqlmodel import SQLModel, Field, create_engine, Session, select

class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int

class Courses(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    duration: int

engine = create_engine("sqlite:///student.db")

# SQLModel.metadata.create_all(engine)


# ====>> Insert Students

# with Session(engine) as session:
#     student = Student(name="Umar", age=18)

#     session.add(student)

#     session.commit()

#     session.refresh(student)

#     print(student.model_dump())


# ====>> Select Data

# with Session(engine) as session:
#     # statement = select(Student)

#     statement = select(Student).where(Student.id == 8)

#     students = session.exec(statement).first()

#     # for student in students:
#     #     print(student.model_dump())

#     print(students)


# ====>> Update students

# with Session(engine) as session:
    # statement = select(Student).where(Student.id == 5)

    # student = session.exec(statement).first()
    
    # student.name = "Usman"

    # session.add(student)

#     session.commit()

#     session.refresh(student)

#     print(student)


# ====>> Delete students

# with Session(engine) as session:
#     # statement = select(Student).where(Student.id == 5)
#     # student = session.exec(statement).first()

#     # session.delete(student)

#     # Table delete
#     Student.__table__.drop(engine)

#     session.commit()

#     print("Deleted")


# ====>> Create Perticular Table
with Session(engine) as session:
    Courses.__table__.create(engine)
    print("Table created")