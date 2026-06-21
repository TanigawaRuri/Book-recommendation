from pydantic import BaseModel

class Book(BaseModel):
    name: str
    publisher: str
    author: str
    price: str
    genre: str
    description: str = ""
