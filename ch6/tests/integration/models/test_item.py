import os
from unittest import TestCase
from models.item import ItemModel
from models.store import StoreModel
from db import reset_db


class TestItem(TestCase):
    def setUp(self):
        reset_db()

    def test_crud(self):
        store = StoreModel('testStore')
        item = ItemModel(name='test', price=12.99, store_id=1)
        self.assertIsNone(ItemModel.filter_by_name('test'))

        store.save()
        item.save()
        self.assertIsNotNone(ItemModel.filter_by_name('test'))

        item.delete()
        self.assertIsNone(ItemModel.filter_by_name('test'))
        store.save()

