from falcon import testing
from app import app
from db import reset_db, Session
from models.store import StoreModel
from models.item import ItemModel

class TestItem(testing.TestCase):
    def setUp(self):
        super(TestItem, self).setUp()
        reset_db()
        self.app = app
        self.sess = Session()
        self.simulate_post('/register', params={'name':'test', 'password':'pa55'})
        auth = self.simulate_post('/auth', params={'name':'test', 'password':'pa55'},
                                  headers={'Content-Type':'application/json'})
        self.access_token = auth.json
        # r = self.simulate_get('/', headers=self.access_token)
    def tearDown(self):
        self.sess.close()

    def test_item_not_auth(self):
        r = self.simulate_get('/item/test')
        self.assertEqual(r.status_code, 401)

    def test_item_not_found(self):
        r = self.simulate_get('/item/testStore', headers=self.access_token)
        self.assertEqual(r.status_code, 404)

    def test_item_found(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        self.sess.flush()
        item = ItemModel(name='testItem', price=12.99, store_id=store.id)
        self.sess.add(item)
        self.sess.commit()
        r = self.simulate_get('/item/testItem', headers=self.access_token)
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({'name':'testItem', 'price':12.99}, r.json)

    def test_delete_item(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        self.sess.flush()
        item = ItemModel(name='testItem', price=12.99, store_id=store.id)
        self.sess.add(item)
        self.sess.commit()
        r = self.simulate_delete('/item/testItem', headers=self.access_token)
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({'message':'Item deleted'}, r.json)

    def test_create_item(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        self.sess.flush()
        r = self.simulate_post('/item/test',
                               params={'price':12.99, 'store_id':store.id},
                               headers=self.access_token)
        self.assertEqual(r.status_code, 201)
        self.assertDictEqual({'name':'test', 'price':12.99}, r.json)

    def test_create_duplicate_item(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        self.sess.flush()
        self.simulate_post('/item/test',
                           params={'price':12.99, 'store_id':store.id},
                           headers=self.access_token)
        r = self.simulate_post('/item/test',
                               params={'price':12.99, 'store_id':store.id},
                               headers=self.access_token)
        self.assertEqual(r.status_code, 400)

    def test_put_item(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        self.sess.flush()
        r = self.simulate_put('/item/test',
                              params={'price':12.99, 'store_id':store.id},
                              headers=self.access_token)
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({'name':'test', 'price':12.99}, r.json)

    def test_put_update_item(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        self.sess.flush()
        self.simulate_put('/item/test',
                          params={'price':12.99, 'store_id':store.id},
                          headers=self.access_token)
        r = self.simulate_put('/item/test',
                              params={'price':10.99, 'store_id':store.id},
                              headers=self.access_token)
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({'name':'test', 'price':10.99}, r.json)

    def test_list_item(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        self.sess.flush()
        item = ItemModel(name='testItem', price=12.99, store_id=store.id)
        self.sess.add(item)
        self.sess.commit()
        r = self.simulate_get('/items', headers=self.access_token)
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({'items':[{'name':'testItem', 'price':12.99}]}, r.json)


