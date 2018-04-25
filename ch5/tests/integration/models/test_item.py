import os
os.environ['DB_URI'] = 'sqlite:///'

from unittest import TestCase
from models.item import ItemModel
from db import reset_db


class TestItem(TestCase):
    def setUp(self):
        reset_db()

    def test_crud(self):
        item = ItemModel(name='test', price=12.99)
        self.assertIsNone(ItemModel.filter_by_name('test'))

        item.save()
        self.assertIsNotNone(ItemModel.filter_by_name('test'))

        item.delete()
        self.assertIsNone(ItemModel.filter_by_name('test'))

