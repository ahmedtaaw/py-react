# allows us to work with typing in python
from typing import List
# the fastapi framework import
from fastapi import FastAPI

from pydantic import BaseModel

# this how we intialize it
app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age:int

DB: List[Person]=[
    Person(id=1, name="Pablo", age = 23),
    Person(id=2, name="Tawfik", age = 22)
]


# anotation and methods
@app.get("/api")
def read_root():
    # return {"Hello": "World"}
    return DB


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}