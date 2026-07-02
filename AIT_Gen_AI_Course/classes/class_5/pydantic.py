from pydantic import BaseModel

class Students(BaseModel):
    name: str
    age: int
    is_active: bool
    
ali = Students(name="Ali", age=20, is_active=True)
