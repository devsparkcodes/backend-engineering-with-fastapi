from sqlmodel import SQLModel, Field, create_engine, Session

class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int

DATABASE_URL = "sqlite:///student.db"

engine = create_engine(DATABASE_URL)



def get_session():
    with Session(engine) as session:
        

        Student.__table__create(engine)
        yield session

        print("Table created")
        

get_session()