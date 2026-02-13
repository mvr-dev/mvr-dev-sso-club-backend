from sqlalchemy import Column, Date, ForeignKey, Integer, String, Boolean, DateTime
from core.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"))
    organization_code = Column(String,nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    registration_date = Column(Date)
    status = Column(Integer, nullable=False, default=2)
