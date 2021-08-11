from typing import Optional
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from app.src.database.models import books


# Shared properties
class BookBase(BaseModel):
    title: Optional[str] = None
    isbn: Optional[str] = None


class BookCreate(BookBase):
    title: str
    isbn: str


class BookUpdate(BookBase):
    pass


BookInDB = sqlalchemy_to_pydantic(books.Book)
