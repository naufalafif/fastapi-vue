from app.src.database import Base
from sqlalchemy import Column, String, Integer, Boolean
from datetime import datetime


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, index=True, primary_key=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    avatar = Column(String)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
