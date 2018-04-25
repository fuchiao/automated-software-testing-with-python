from falcon import testing
from app import app

class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()
        self.app = app

class TestHome(MyTestCase):
    def test_home(self):
        expect = {'message':'hello'}
        result = self.simulate_get('/')
        self.assertDictEqual(result.json, expect)
