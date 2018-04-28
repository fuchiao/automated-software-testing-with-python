from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship, backref
from db import Base, Session

class StoreModel(Base):
    __tablename__ = 'stores'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    items = relationship('ItemModel', backref='items', lazy='dynamic')

    def json(self):
        return {
            'name':self.name,
            'items':[item.json() for item in self.items.all()]
        }
