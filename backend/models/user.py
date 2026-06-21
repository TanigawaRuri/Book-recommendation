from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str

class Userlogin(BaseModel):
    email: str
    password: str