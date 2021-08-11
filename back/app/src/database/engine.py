from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.src.core import config

engine = create_engine(config.DB_DSN)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
