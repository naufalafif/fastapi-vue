from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.src.crud.base import CRUDBase
from app.src.database.models.books import Book
from app.src.schema.books_schema import BookCreate, BookUpdate


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate]):
    def create_with_author(
        self, db: Session, *, obj_in: BookCreate, author_id: int
    ) -> Book:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, author_id=author_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_author(
        self, db: Session, *, author_id: int, skip: int = 0, limit: int = 100
    ) -> List[Book]:
        return (
            db.query(self.model)
            .filter(Book.author_id == author_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


book = CRUDBook(Book)
