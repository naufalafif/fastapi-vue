from app.src.database import Base
from sqlalchemy import Column, Integer, DateTime, String, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum


class LanguageEnum(enum.Enum):
    en = "english"
    id = "indonesia"


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    original_language = Column(Enum(LanguageEnum))
    created_date = Column(DateTime, default=datetime.now)
    books = relationship("Book", back_populates="author")
