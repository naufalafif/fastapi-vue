from typing import Any, List

from fastapi import  Depends, HTTPException
from sqlalchemy.orm import Session

from app.src import crud, schema as schemas
from app.src.database import models
from app.src.router import deps
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()


@cbv(router)
class SuperUserClassView:
    current_user: models.User = Depends(deps.get_current_active_superuser)

    @router.get("/", response_model=List[schemas.User])
    def read_users(
        self,
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100
    ) -> Any:
        """
        Retrieve users.
        """
        users = crud.user.get_multi(db, skip=skip, limit=limit)
        return users


    @router.post("/")
    def create_user(
        self,
        *,
        db: Session = Depends(deps.get_db),
        user_in: schemas.UserCreate
    ) -> Any:
        """
        Create new user.
        """
        user = crud.user.get_by_email(db, email=user_in.email)
        if user:
            raise HTTPException(
                status_code=400,
                detail="The user with this username already exists in the system.",
            )
        user = crud.user.create(db, obj_in=user_in)
        return user

    @router.get("/{user_id}", response_model=schemas.User)
    def read_user_by_id(
        self,
        user_id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
        db: Session = Depends(deps.get_db),
    ) -> Any:
        """
        Get a specific user by id.
        """
        user = crud.user.get(db, id=user_id)
        if user == current_user:
            return user
        if not crud.user.is_superuser(current_user):
            raise HTTPException(
                status_code=400, detail="The user doesn't have enough privileges"
            )
        return user


    @router.put("/{user_id}", response_model=schemas.User)
    def update_user(
        *,
        db: Session = Depends(deps.get_db),
        user_id: int,
        user_in: schemas.UserUpdate,
        current_user: models.User = Depends(deps.get_current_active_superuser),
    ) -> Any:
        """
        Update a user.
        """
        user = crud.user.get(db, id=user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="The user with this username does not exist in the system",
            )
        user = crud.user.update(db, db_obj=user, obj_in=user_in)
        return user

