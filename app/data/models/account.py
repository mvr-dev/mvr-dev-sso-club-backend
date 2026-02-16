from datetime import date
from pydantic import BaseModel


class Account(BaseModel):
    id : int | None = None
    user_id : int
    organization_code : str | None = "1234"
    login : str
    password : str
    registration_date : date = date.today()
    status : int
    
