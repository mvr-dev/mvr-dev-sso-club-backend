from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreateRequest(BaseModel):
    surname : str
    name :  str
    patronymic : Optional[str]
    birthday : Optional[date]

    phone : str
    email : str
    
    region : Optional[str]
    city : Optional[str]
    street : Optional[str]
    house : Optional[str]


    password : str
    email : EmailStr
