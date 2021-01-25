from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from app.users.forms import UserUpdateForm

from app.users.models import User

from .forms import SignUpForm


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
            # messages.success(request, f"Votre compte a bien été crée!")
            return redirect("profile")
        else:
            return render(request, "users/register.html", {"form": form})
    else:
        form = SignUpForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):

    if request.method == "POST":
        user_form = UserUpdateForm(
            request.POST, request.FILES, instance=request.user
        )
        if user_form.is_valid():
            user_form.save()
            # messages.success(request, f"Your account has been updated!")
            return redirect("/")
    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {"user_form": user_form}
    return render(request, "users/profile.html", context)


def activate(request, uidb64):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        user.is_active = True
        user.save()

        messages.success(
            request, f'{"Votre compte a été activé, vous pouvez vous logger!"}'
        )
        return redirect("login")
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        None
