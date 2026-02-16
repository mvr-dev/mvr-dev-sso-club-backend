from sqlalchemy import Column, Date, Integer, String, Boolean, DateTime
from core.database import Base

class User(Base):
    __tablename__ = "person"

    id = Column(Integer, name="person_id" ,primary_key=True, index=True, autoincrement=True)
    user_code = Column(String, name="person_code",unique=True, nullable=False)

    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)

    name = Column(String, unique=False, nullable=False)
    surname = Column(String, unique=False,nullable=False)
    patronymic = Column(String,unique=False,nullable=False)

    birthday = Column(Date,name="birth_date")
    clone_code = Column(String, default='5410')

    region = Column(String)
    city = Column(String)
    street = Column(String)
    house = Column(String)
