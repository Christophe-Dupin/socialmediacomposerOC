from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post


def login(request):
    return render(request, "login.html")


def home(request):
    return render(request, "posts/home.html")


@login_required
def all_posts_queue(request):
    return render(request, "posts/posts.html")


@login_required
def all_posts_send(request):
    return render(request, "posts/posts_history.html")
