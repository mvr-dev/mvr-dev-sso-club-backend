from pydantic import BaseModel
from typing import Optional
from datetime import date

class User(BaseModel):
    id : Optional[int] = None
    user_code : str

    #fullname
    surname : str
    name : str
    patronymic : str
    birthday : date

    region : str
    city : str
    street : str
    house : str
    
    email : str
    phone : str

    clone_code : str = '5410'



    

