from fastapi import Depends, File, UploadFile
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.src.schema import books_schema as schema
from typing import List
from app.src.database import models
from app.src.router import deps
from app.src.core import config
import cloudinary
import cloudinary.uploader

cloudinary.config( 
  cloud_name = config.CLOUDINARY_CLOUDNAME, 
  api_key = config.CLOUDINARY_APIKEY, 
  api_secret = config.CLOUDINARY_SECRET 
)

router = InferringRouter()


@cbv(router)
class UtilsClassView:
    current_user: models.User = Depends(deps.get_current_active_user)

    @router.post("/uploadfile")
    async def upload_file(self, file: UploadFile = File(...)):
        file_bytes = await file.read()
        cloudinary_response = cloudinary.uploader.upload(bytearray(file_bytes))
        return {
          "url": cloudinary_response.get('secure_url')
        }
