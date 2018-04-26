from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base, Session

class ItemModel(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    price = Column(Float(precision=2))
    store_id = Column(Integer, ForeignKey('stores.id'))
    store = relationship('StoreModel', foreign_keys=[store_id])

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

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

    @classmethod
    def filter_by_name(cls, name):
        sess = Session()
        item = sess.query(cls).filter(ItemModel.name==name).first()
        sess.close()
        return item

    @classmethod
    def filter_by_store(cls, store_id):
        sess = Session()
        items = sess.query(cls).filter(ItemModel.store_id==store_id).all()
        sess.close()
        return items

    def json(self):
        return {'name':self.name, 'price':self.price}

