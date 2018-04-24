from unittest import TestCase
from blog import Blog

class TestBlog(TestCase):
    def test_create_post(self):
        b = Blog('TestTitle', 'TestAuthor')
        b.create_post('TestPostTitle', 'TestContent')
        self.assertEqual(b.posts[0].title, 'TestPostTitle')
        self.assertEqual(b.posts[0].content, 'TestContent')

    def test_json_with_post(self):
        b = Blog('TestTitle', 'TestAuthor')
        b.create_post('TestPostTitle', 'TestContent')
        self.assertDictEqual(b.json(), {'title':'TestTitle', 'author':'TestAuthor', 'posts':[{'title':'TestPostTitle', 'content':'TestContent'}]})
