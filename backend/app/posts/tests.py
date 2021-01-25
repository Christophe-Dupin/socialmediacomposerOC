from django.test import TestCase
from app.posts.models import Post
class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(body='a body here')

    def test_body_content(self):
        post = Post.objects.get(id=1)
        expected_object_body = f'{post.body}'
        self.assertEqual(expected_object_body, 'a body here')
