from unittest import TestCase
from blog import Blog

class TestBlog(TestCase):
    def test_blog(self):
        b = Blog('TestTitle', 'TestAuthor')
        self.assertEqual(b.title, 'TestTitle')
        self.assertEqual(b.author, 'TestAuthor')
        self.assertEqual(len(b.posts), 0)
        self.assertListEqual(b.posts, [])

    def test_json(self):
        b = Blog('TestTitle', 'TestAuthor')
        self.assertDictEqual(b.json(),
                             {'title':'TestTitle', 'author':'TestAuthor','posts':[]})

    def test_repr(self):
        b = Blog('TestTitle', 'TestAuthor')
        self.assertEqual(repr(b), 'TestTitle by TestAuthor (0 posts)')

