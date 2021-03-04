from django import forms
from config.settings.base import DATE_INPUT_FORMATS

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("body", "socialmedia", "schedule_time")
