from unittest import TestCase
from models.user import UserModel
from db import reset_db, Session

class TestUser(TestCase):
    def setUp(self):
        reset_db()
        self.sess = Session()

    def tearDown(self):
        self.sess.close()

    def test_crud(self):
        user = UserModel(name='testUser', password='pa55')
        self.assertEqual(self.sess.query(UserModel).count(), 0)

        self.sess.add(user)
        self.sess.commit()
        self.assertEqual(self.sess.query(UserModel).count(), 1)

        self.sess.delete(user)
        self.sess.commit()
        self.assertEqual(self.sess.query(UserModel).count(), 0)

