import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
DB_URI = os.getenv('DB_URI', 'sqlite:///')
DB_URI='mysql+pymysql://root:pa55word@127.0.0.1/ch6'
DB_URI='postgresql://postgres:pa55@127.0.0.1:5432/ch6'
print('connect db {}'.format(DB_URI))

engine = create_engine(DB_URI)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def reset_db():
    from models.store import StoreModel
    from models.item import ItemModel
    from models.user import UserModel
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__=='__main__':
    # e.g. env DB_URI=sqlite:///item.db python db.py
    print('drop and create {}'.format(DB_URI))
    from models.store import StoreModel
    from models.item import ItemModel
    from models.user import UserModel
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
