from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id : Optional[int] = None
    surname : str
    name : str
    password : str
    

