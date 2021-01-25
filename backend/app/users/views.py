from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from app.users.forms import UserUpdateForm

# from django.contrib import messages
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
