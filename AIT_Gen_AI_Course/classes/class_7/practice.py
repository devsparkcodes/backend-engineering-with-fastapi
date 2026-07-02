# Exercise 1
from fastapi import FastAPI
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)
    in_stock: bool = True