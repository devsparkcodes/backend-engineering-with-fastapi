from sqlmodel import SQLModel, Field, create_engine, Session

class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int
    is_active: bool = True
    
engine = create_engine("sqlite:///school.db", echo=True)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    student = Student(name="Ahmed", age=20, is_active=False)
    session.add(student)
    session.commit()
    
    print(student.id)
    print("hello")
    print(student.id)
    print(student.name)
    print(student.age)
    # session.refresh(student)
    
    
    
    
    
# Spec-Driven Development

# Constitution
# Specification
# Planning
# Analyzing Planning
# Plan convert in terms of tasks
# Implementaion

# github.com/panaversity/spec-kit-plus
# https://agentfactory.panaversity.org/