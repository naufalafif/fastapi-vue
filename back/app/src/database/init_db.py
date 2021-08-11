from sqlalchemy.orm import Session

from app.src import crud, schema as schemas
from app.src.core import config

def init_db(db: Session) -> None:

    user = crud.user.get_by_email(db, email=config.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=config.FIRST_SUPERUSER,
            password=config.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
