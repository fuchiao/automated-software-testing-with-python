from unittest import TestCase
from models.store import StoreModel
from models.item import ItemModel
from db import reset_db, Session

class TestStore(TestCase):
    def setUp(self):
        reset_db()

    def test_create_store(self):
        store = StoreModel('testStore')
        self.assertListEqual(store.items.all(), [])

    def test_crud(self):
        store = StoreModel('testStore')
        self.assertIsNone(StoreModel.find_by_name('testStore'))

        store.save()
        self.assertIsNotNone(StoreModel.find_by_name('testStore'))

        store.delete()
        self.assertIsNone(StoreModel.find_by_name('testStore'))

    def test_store_relationship(self):
        store = StoreModel('testStore')
        item = ItemModel('testItem', 12.99, 1)
        store.save()
        item.save()
        items = ItemModel.filter_by_store(1)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].name, 'testItem')

    def test_store_json(self):
        store = StoreModel('testStore')
        expected = {
            'name':'testStore',
            'items':[],
        }
        self.assertEqual(store.json(), expected)
