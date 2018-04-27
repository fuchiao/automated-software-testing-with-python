from unittest import TestCase

from models.item import ItemModel

class TestItem(TestCase):
    def test_create_item(self):
        item = ItemModel(name='test', price=12.99, store_id=1)
        self.assertEqual(item.name, 'test')
        self.assertEqual(item.price, 12.99)

    def test_item_json(self):
        item = ItemModel(name='test', price=12.99, store_id=1)
        expected = {'name':'test', 'price':12.99}
        self.assertEqual(item.json(), expected)
