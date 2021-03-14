from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from allauth.socialaccount.models import SocialAccount

from app.users.forms import UserUpdateForm
from app.users.models import User

from .forms import SignUpForm


def login(request):
    return render(request, "users/login.html")


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
            user.first_name = form.cleaned_data["first_name"]
            user.first_name = form.cleaned_data["last_name"]
            user.is_active = False

            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activer votre compte."
            to_email = form.cleaned_data.get("email")
            message = render_to_string(
                "users/user_active_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                },
            )
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            messages.success(
                request,
                f'{"Votre compte a bien été crée, un mail vous a été envoyé pour confirmer votre inscription!"}',
            )
            return redirect("profile")
        else:
            return render(
                request,
                "users/register.html",
                {"form": form},
            )
    else:
        form = SignUpForm()

    return render(request, "users/register.html", {"form": form})

    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):

    if request.method == "POST":
        user_form = UserUpdateForm(
            request.POST, request.FILES, instance=request.user
        )
        print(request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f'{"Your account has been updated!"}')
            return redirect("all_posts_queue")
        else:
            print("tutu")
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


@login_required
def manage_channels(request):
    social_account = SocialAccount.objects.filter(user=request.user)
    return render(
        request, "users/accounts.html", {"social_account": social_account}
    )


@login_required
def delete_channels(request, provider):
    provider
    social_account = SocialAccount.objects.filter(user=request.user)
    return render(
        request, "users/accounts.html", {"social_account": social_account}
    )


def privacy_policy(request):
    return render(request, "users/privacy_policy.html")
