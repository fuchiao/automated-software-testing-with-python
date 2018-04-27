from unittest import TestCase
from models.store import StoreModel

class TestStore(TestCase):
    def test_create_store(self):
        store = StoreModel('testStore')
        self.assertEqual(store.name, 'testStore')
