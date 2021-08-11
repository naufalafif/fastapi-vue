from fastapi import Depends, Response, status, HTTPException, Request
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.src.schema import books_schema as schema
from typing import List
from app.src.database import models
from app.src.router import deps
from app.src.crud import book as crud_book
from app.src.database import session_manager
from app.src.schema import BookCreate

router = InferringRouter()


@cbv(router)
class BookClassView:
    current_user: models.User = Depends(deps.get_current_active_user)

    @router.get("/", response_model=List[schema.BookInDB])
    def get_books(self, skip: int = 0, limit: int = 20):
        with session_manager() as db:
            books = crud_book.get_multi(db=db, limit=limit, skip=skip)
            return books

    @router.get("/{book_id}", response_model=schema.BookInDB)
    def get_book(self, book_id: int):
        with session_manager() as db:
            book = crud_book.get(db=db, id=book_id)
            if book is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found")
            return book

    @router.post("/", response_model=schema.BookInDB)
    def create_book(self, data: schema.BookCreate):
        with session_manager() as db:
            created_book = crud_book.create(db=db, obj_in=data)
            return created_book


    @router.delete("/{book_id}", response_model=schema.BookInDB)
    def delete_book(self, book_id: int):
        with session_manager() as db:
            deleted_book = crud_book.remove(db=db, id=book_id)
            return deleted_book
