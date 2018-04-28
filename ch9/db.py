import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float, text
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
DB_USER='postgres'
DB_PASS='pa55'
DB_HOST='127.0.0.1'
DB_PORT='5432'
DB_NAME='ch9'
DB_ENGINE='postgresql://{}:{}@{}:{}'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT)
DB_URI='postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
print('connect db {}'.format(DB_URI))

engine = create_engine(DB_ENGINE, isolation_level='AUTOCOMMIT')
engine.execute("DROP DATABASE IF EXISTS {}".format(DB_NAME))
engine.execute("CREATE DATABASE {}".format(DB_NAME))
engine = create_engine(DB_URI)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def reset_db():
    from models.store import StoreModel
    from models.item import ItemModel
    from models.user import UserModel
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    
