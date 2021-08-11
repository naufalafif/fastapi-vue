from typing import Any

from fastapi import Body, Depends
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app.src import crud, schema as schemas
from app.src.database import models
from app.src.router import deps
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()


@cbv(router)
class UserClassView:
    current_user: models.User = Depends(deps.get_current_active_user)

    @router.put("/me", response_model=schemas.User)
    def update_user_me(
        self,
        *,
        db: Session = Depends(deps.get_db),
        password: str = Body(None),
        full_name: str = Body(None),
        email: EmailStr = Body(None),
        avatar: str = Body(None),
    ) -> Any:
        """
        Update own user.
        """
        current_user_data = jsonable_encoder(self.current_user)
        user_in = schemas.UserUpdate(**current_user_data)
        print(user_in)
        if password is not None:
            user_in.password = password
        if full_name is not None:
            user_in.full_name = full_name
        if email is not None:
            user_in.email = email
        if avatar is not None:
            user_in.avatar = avatar
        user = crud.user.update(db, db_obj=self.current_user, obj_in=user_in)
        return user


    @router.get("/me", response_model=schemas.User)
    def read_user_me(
        self,
        db: Session = Depends(deps.get_db),
    ) -> Any:
        """
        Get current user.
        """
        return self.current_user

