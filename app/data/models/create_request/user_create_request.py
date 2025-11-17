from pydantic import BaseModel

class UserCreateRequest(BaseModel):
    name : str
    surname : str
    password : str