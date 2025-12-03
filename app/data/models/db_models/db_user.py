from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from core.database import Base

class User(Base):  # Наследуется от SQLAlchemy Base
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, unique=False, nullable=False)
    surname = Column(String, unique=False,nullable=False)
    patronymic = Column(String,unique=False,nullable=False)
    hashed_password = Column(String, nullable=False)