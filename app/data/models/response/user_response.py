from datetime import date
from typing import Optional
from pydantic import BaseModel

class UserResponse(BaseModel):
    id : int
    surname : str
    name : str
    patronymic : str
    email : str
    
    region : Optional[str]
    city : Optional[str]
    street : Optional[str]
    house : Optional[str]
    birthday : Optional[date]
    phone : str
    