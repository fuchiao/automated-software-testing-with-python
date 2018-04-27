from unittest import TestCase
from models.store import StoreModel
from models.item import ItemModel
from db import reset_db, Session

class TestStore(TestCase):
    def setUp(self):
        reset_db()
        self.sess = Session()

    def tearDown(self):
        self.sess.close()

    def test_create_store(self):
        store = StoreModel('testStore')
        self.assertEqual(store.items.count(), 0)

    def test_crud(self):
        store = StoreModel('testStore')
        self.assertEqual(self.sess.query(StoreModel).filter(StoreModel.name=='testStore').count(), 0)

        self.sess.add(store)
        self.sess.commit()
        self.assertEqual(self.sess.query(StoreModel).filter(StoreModel.name=='testStore').count(), 1)

        self.sess.delete(store)
        self.sess.commit()
        self.assertEqual(self.sess.query(StoreModel).filter(StoreModel.name=='testStore').count(), 0)

    def test_store_relationship(self):
        store = StoreModel('testStore')
        item = ItemModel('testItem', 12.99, 1)
        self.sess.add(store)
        self.sess.add(item)
        self.sess.commit()
        items = self.sess.query(ItemModel).filter(ItemModel.store_id==1).all()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].name, 'testItem')

    def test_store_json(self):
        store = StoreModel('testStore')
        expected = {
            'name':'testStore',
            'items':[],
        }
        self.assertEqual(store.json(), expected)
