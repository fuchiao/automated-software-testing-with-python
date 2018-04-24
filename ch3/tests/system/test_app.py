from unittest import TestCase
from unittest.mock import patch
import app

class TestApp(TestCase):
    def test_menu(self):
        with patch('builtins.input', return_value='q') as mocked_input:
                app.menu()
                mocked_input.assert_called_with(app.PROMPT)

    def test_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'newBlog', 'testUser', 'q')
            app.menu()
            self.assertIsNotNone(app.blogs['newBlog'])
            self.assertEqual(app.blogs['newBlog'].title, 'newBlog')
            self.assertEqual(app.blogs['newBlog'].author, 'testUser')

    def test_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'newBlog', 'testUser',
                                        'p', 'newBlog', 'newPost', 'testContent', 'q')
            app.menu()
            self.assertEqual(app.blogs['newBlog'].posts[0].title, 'newPost')
            self.assertEqual(app.blogs['newBlog'].posts[0].content, 'testContent')

    def test_list_blogs(self):
        with patch('app.list_blogs') as mocked_list_blogs:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('l', 'q')
                app.menu()
                mocked_list_blogs.assert_called()
            
    def test_read_blog(self):
        with patch('app.read_blog') as mocked_read_blog:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('c', 'blogTitle', 'user',
                                            'r', 'blogTitle', 'q')
                app.menu()
                mocked_read_blog.assert_called()
