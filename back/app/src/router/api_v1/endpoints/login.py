from datetime import timedelta
from typing import Any

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.src.database import session_manager

from app.src import crud, schema as schemas
from app.src.database import models
from app.src.router import deps
from app.src.core import security
from app.src.core import config



router = InferringRouter()


@cbv(router)
class LoginClassView:

  @router.post("/access-token", response_model=schemas.Token)
  def login_access_token(
      self, form_data: OAuth2PasswordRequestForm = Depends()
  ) -> Any:
      """
      OAuth2 compatible token login, get an access token for future requests
      """

      with session_manager() as db:
        user = crud.user.authenticate(
            db, email=form_data.username, password=form_data.password
        )
      
      if not user:
          raise HTTPException(status_code=400, detail="Incorrect email or password")
      elif not crud.user.is_active(user):
          raise HTTPException(status_code=400, detail="Inactive user")
      access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
      return {
          "access_token": security.create_access_token(
              user.id, expires_delta=access_token_expires
          ),
          "token_type": "bearer",
      }


  @router.get("/info")
  def login_info(self, current_user: models.User = Depends(deps.get_current_active_user)) -> Any:
    """
    Login info
    """

    response = {
        "roles": ['admin' if current_user.is_superuser else 'editor'],
        "introduction": f'I am a {current_user.full_name}',
        "avatar": current_user.avatar,
        "name": current_user.full_name
    }
    return {'data': response}