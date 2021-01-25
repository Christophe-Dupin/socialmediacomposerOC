from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class User(AbstractUser):
    image = models.ImageField(default="default.jpg", upload_to="image")

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        instance = super(User, self).save(**kwargs)
        pil_image = Image.open(self.image.path)
        resized_image = pil_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(self.image.path)
        return instance
