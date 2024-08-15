# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, DeclarativeBase
# from sqlalchemy import Column, Integer,String
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///taskmanager.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = "user"
#
#     id = Column(Integer,primary_key = True)
#     username = Column(String)
#     password = Column(String)