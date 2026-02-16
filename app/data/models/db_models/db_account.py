from sqlalchemy import Column, Date, ForeignKey, Integer, String, Boolean, DateTime
from core.database import Base

class Account(Base):
    __tablename__ = "account"

    id = Column(Integer,name="account_id", primary_key=True, autoincrement=True)
    user_id = Column(Integer,ForeignKey("person.person_id",ondelete="CASCADE"),name="person_id")
    organization_code = Column(String,nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String,name="password_hash" ,nullable=False)
    registration_date = Column(Date)
    status = Column(Integer, nullable=False, default=2)
