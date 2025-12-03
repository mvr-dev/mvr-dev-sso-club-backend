from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreateRequest(BaseModel):
    surname : str
    name : str
    patronymic : Optional[str]
    password : str
    email : EmailStr