from falcon import testing
from app import app
from db import reset_db, Session
from models.store import StoreModel
from models.item import ItemModel

class TestStore(testing.TestCase):
    def setUp(self):
        super(TestStore, self).setUp()
        reset_db()
        self.app = app
        self.sess = Session()
        self.simulate_post('/register', params={'name':'test', 'password':'pa55'})
        auth = self.simulate_post('/auth', params={'name':'test', 'password':'pa55'},
                                  headers={'Content-Type':'application/json'})
        self.headers={'Authorization':'Bearer {}'.format(auth.json['access_token'])}
        # r = self.simulate_get('/', headers=self.access_token)
    def tearDown(self):
        self.sess.close()

    def test_store_not_found(self):
        r = self.simulate_get('/store/test', headers=self.headers)
        self.assertEqual(r.status_code, 404)

    def test_store_found(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        r = self.simulate_get('/store/testStore', headers=self.headers)
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({'name':'testStore', 'items':[]}, r.json)

    def test_store_with_items_found(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        self.sess.flush()
        item = ItemModel(name='testItem', price=12.99, store_id=store.id)
        self.sess.add(item)
        self.sess.commit()
        r = self.simulate_get('/store/testStore', headers=self.headers)
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({'name':'testStore',
                              'items':[{'name':'testItem', 'price':12.99}]},
                              r.json)

    def test_delete_store(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        r = self.simulate_delete('/store/testStore', headers=self.headers)
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({'message':'Store deleted'}, r.json)

    def test_create_store(self):
        r = self.simulate_post('/store/test', headers=self.headers)
        self.assertEqual(r.status_code, 201)
        self.sess.query(StoreModel).filter(StoreModel.name=='test').first()
        self.assertDictEqual({'name':'test', 'items':[]}, r.json)

    def test_create_duplicate_store(self):
        self.simulate_post('/store/test', headers=self.headers)
        r = self.simulate_post('/store/test', headers=self.headers)
        self.assertEqual(r.status_code, 400)

    def test_list_store(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        r = self.simulate_get('/stores', headers=self.headers)
        self.assertDictEqual({'stores':[{'name':'testStore', 'items':[]}]}, r.json)

    def test_list_store_with_item(self):
        store = StoreModel(name='testStore')
        self.sess.add(store)
        self.sess.commit()
        self.sess.flush()
        item = ItemModel(name='testItem', price=12.99, store_id=store.id)
        self.sess.add(item)
        self.sess.commit()
        r = self.simulate_get('/stores', headers=self.headers)
        self.assertDictEqual({
            'stores':[{
                'name':'testStore',
                'items':[{'name':'testItem', 'price':12.99}]
            }]}, r.json)

