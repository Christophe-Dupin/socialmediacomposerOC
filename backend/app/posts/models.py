from django.db import models
from app.users.models import User


class SocialMedia(models.Model):
    socialmedia = models.CharField(max_length=255)

    def __str__(self):
        return self.socialmedia


class Post(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_queue = models.BooleanField(default=True)
    is_send = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    socialmedia = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
