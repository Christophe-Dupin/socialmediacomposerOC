from django.test import TestCase
from app.posts.models import Post, SocialMedia
from app.users.models import User


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        socialmedia = SocialMedia(socialmedia="linkedin")
        socialmedia.save()
        author = User.objects.create_user(
            username="chris",
            email="chris@socialmediacomposer.com",
            password="testing1234",
        )
        author.save()
        post = Post(
            body="Mon post de test",
            author=author,
            schedule_time="2021-09-07 09:23",
        )
        post.save()
        print(post.id)
        post.socialmedia.add(socialmedia.id)

    def test_body_content(self):
        post = Post.objects.get(id=1)
        expected_object_body = f"{post.body}"
        self.assertEqual(expected_object_body, "Mon post de test")
