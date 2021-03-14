from django import forms
from config.settings.base import DATE_INPUT_FORMATS
from django.forms import DateTimeField
from .models import Post


class PostForm(forms.ModelForm):
    schedule_time = DateTimeField(
        input_formats=["%d/%m/%Y %H:%M"],
        widget=forms.widgets.DateTimeInput(format="%d/%m/%Y %H:%M'"),
    )

    class Meta:
        model = Post
        fields = ("body", "socialmedia", "schedule_time")
