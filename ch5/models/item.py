from sqlalchemy import Column, Integer, String, Float
from db import Base, Session

class ItemModel(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    price = Column(Float(precision=2))

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
    def filter_by_name(name):
        sess = Session()
        item = sess.query(ItemModel).filter(ItemModel.name==name).first()
        sess.close()
        return item

    def json(self):
        return {'name':self.name, 'price':self.price}

