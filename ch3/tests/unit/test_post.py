from unittest import TestCase
from post import Post

class TestPost(TestCase):
    def test_post(self):
        p = Post('TestTitle', 'TestContent')
        self.assertEqual(p.title, 'TestTitle')
        self.assertEqual(p.content, 'TestContent')

    def test_post_json(self):
        p = Post('TestTitle', 'TestContent')
        self.assertDictEqual(p.json(),
                             {'title':'TestTitle',
                              'content':'TestContent'})
