from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserUpdateRequest(BaseModel):
    surname : str
    name :  str
    patronymic : Optional[str] = None
    birthday : Optional[date] = None

    phone : str
    
    region : Optional[str] = None
    city : Optional[str] = None
    street : Optional[str] = None
    house : Optional[str] = None