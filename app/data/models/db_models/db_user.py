from sqlalchemy import Column, Date, Integer, String, Boolean, DateTime
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_code = Column(String, unique=True, nullable=False)

    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)


    name = Column(String, unique=False, nullable=False)
    surname = Column(String, unique=False,nullable=False)
    patronymic = Column(String,unique=False,nullable=False)

    birthday = Column(Date)
    clone_code = Column(String, default='5410')

    region = Column(String)
    city = Column(String)
    street = Column(String)
    house = Column(String)
