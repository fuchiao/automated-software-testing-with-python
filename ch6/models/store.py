from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship, backref
from db import Base, Session

class StoreModel(Base):
    __tablename__ = 'stores'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    items = relationship('ItemModel', backref='items', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def save(self):
        sess = Session()
        sess.add(self)
        sess.commit()
        sess.close()

    def delete(self):
        sess = Session()
        sess.delete(self)
        sess.commit()
        sess.close()

    @staticmethod
    def find_by_name(name):
        sess = Session()
        store = sess.query(StoreModel).filter(StoreModel.name==name).first()
        sess.close()
        return store

    def json(self):
        return {
            'name':self.name,
            'items':[item.json() for item in self.items.all()]
        }
