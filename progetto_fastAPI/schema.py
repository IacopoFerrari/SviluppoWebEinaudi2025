from pydantic import BaseModel


class User(BaseModel):
    password: str
    username: str

class UserCreate(BaseModel):
    password: str
    username: str
    password_confirm: str
