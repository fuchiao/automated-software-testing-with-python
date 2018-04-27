from unittest import TestCase
from models.user import UserModel

class TestUser(TestCase):
    def test_create_user(self):
        user = UserModel(name='testUser', password='pa55')
        self.assertEqual(user.name, 'testUser')
        self.assertEqual(user.password, 'pa55')
