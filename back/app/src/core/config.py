from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

# DB
DB_DSN = config("DB_DSN", default='sqlite:///database.db')

# Security
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=60*24*1)
SECRET_KEY = config("SECRET_KEY", default='09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7')


# General
API_PREFIX = config("API_PREFIX", default="")
PROJECT_NAME = config("PROJECT_NAME", default="Starx Notification Service")
DEBUG = config("DEBUG", cast=bool, default=True)
VERSION = config("VERSION", default="")

FIRST_SUPERUSER = config("FIRST_SUPERUSER", default="naufalafif58@gmail.com")
FIRST_SUPERUSER_PASSWORD = config("FIRST_SUPERUSER_PASSWORD", default="admin")

# Cloudinary
CLOUDINARY_CLOUDNAME = config("CLOUDINARY_CLOUDNAME", default="dgkfkshnx")
CLOUDINARY_APIKEY = config("CLOUDINARY_APIKEY", default="936242461776631")
CLOUDINARY_SECRET = config("CLOUDINARY_SECRET", default="Jn1aVXk6G2Sf90uW2LYnok3ppfA")
