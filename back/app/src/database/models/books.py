from app.src.database import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String, index=True)
    isbn = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("author.id"))
    author = relationship("Author", back_populates="books")
    created_date = Column(DateTime, default=datetime.now)
    updated_date = Column(DateTime, onupdate=datetime.now)
