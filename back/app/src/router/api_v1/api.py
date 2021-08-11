from fastapi import APIRouter
from .endpoints.book import router as book
from .endpoints.login import router as login
from .endpoints.users import router as users
from .endpoints.user import router as user
from .endpoints.utils import router as utils

router = APIRouter()

router.include_router(book, prefix='/book', tags=['Books'])
router.include_router(login, prefix='/login', tags=['Login'])
router.include_router(users, prefix='/users', tags=['Users'])
router.include_router(user, prefix='/user', tags=['User'])
router.include_router(utils, prefix='/utils', tags=['Utils'])