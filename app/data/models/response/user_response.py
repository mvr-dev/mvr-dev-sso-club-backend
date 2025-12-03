from pydantic import BaseModel

class UserResponse(BaseModel):
    id : int
    surname : str
    name : str
    patronymic : str
    email : str
    