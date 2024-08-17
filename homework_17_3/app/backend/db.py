# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///taskmanager.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
#
# from .db import SessionLocal
#
# async def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = "user"
#
#     id = Column(Integer,primary_key = True)
#     username = Column(String)
#     password = Column(String)