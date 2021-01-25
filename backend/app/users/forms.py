from django import forms

from app.users.models import User


class SignUpForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=100)
    email = forms.EmailField(label="adresse email")
    password = forms.CharField(
        label="mot de passe", max_length=32, widget=forms.PasswordInput
    )


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=100)
    password = forms.CharField(
        label="mot de passe", max_length=32, widget=forms.PasswordInput
    )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]
