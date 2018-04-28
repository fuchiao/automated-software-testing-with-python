from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base, Session

class ItemModel(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    price = Column(Float(precision=2))
    store_id = Column(Integer, ForeignKey('stores.id'))
    store = relationship('StoreModel', foreign_keys=[store_id])

    def json(self):
        return {'name':self.name, 'price':self.price}

