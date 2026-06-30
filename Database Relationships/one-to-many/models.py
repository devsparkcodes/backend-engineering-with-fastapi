from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    recipes: list["Recipe"] = Relationship(back_populates="user")

class Recipe(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    user_id: int = Field(foreign_key="user.id")

    user = Relationship(back_populates="recipes")