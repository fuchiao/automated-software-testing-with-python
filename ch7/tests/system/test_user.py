from falcon import testing
from db import reset_db
from app import app

class TestUser(testing.TestCase):
    def setUp(self):
        super(TestUser, self).setUp()
        reset_db()
        self.app = app

    def test_register_user(self):
        result = self.simulate_post('/register', 
                                    params={'name':'test', 'password':'pa55'})
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json, {'message':'User created successfully'})

    def test_register_and_login(self):
        self.simulate_post('/register', params={'name':'test', 'password':'pa55'})
        ''' FIXME: /auth is not ready
        auth = self.simulate_post('/auth', params={'name':'test', 'password':'pa55'},
                                  headers={'Content-Type':'application/json'})
        self.assertIn('access_token', auth.json)
        '''

    def test_register_duplicate(self):
        self.simulate_post('/register', params={'name':'test', 'password':'pa55'})
        r = self.simulate_post('/register', params={'name':'test', 'password':'pa55'})
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json, {'message':'A user with that username already exists'})

