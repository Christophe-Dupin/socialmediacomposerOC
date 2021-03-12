from django import forms
from config.settings.base import DATE_INPUT_FORMATS
from bootstrap_datepicker_plus import DatePickerInput
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            "schedule_time": DatePickerInput(
                format="%m/%d%Y"
            ),  # python date-time format
        }
        fields = ("body", "socialmedia")


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=["%d/%m/%Y %H:%M"])
