import os
from unittest import TestCase
from models.item import ItemModel
from models.store import StoreModel
from db import reset_db, Session


class TestItem(TestCase):
    def setUp(self):
        reset_db()
        self.sess = Session()

    def tearDown(self):
        self.sess.close()

    def test_crud(self):
        store = StoreModel(name='testStore')
        item = ItemModel(name='test', price=12.99, store_id=1)
        self.assertEqual(self.sess.query(ItemModel).filter(ItemModel.name=='test').count(), 0)

        self.sess.add(store)
        self.sess.add(item)
        self.sess.commit()
        self.assertEqual(self.sess.query(ItemModel).filter(ItemModel.name=='test').count(), 1)

        self.sess.delete(item)
        self.sess.commit()
        self.assertEqual(self.sess.query(ItemModel).filter(ItemModel.name=='test').count(), 0)
        self.sess.delete(store)
        self.sess.commit()

