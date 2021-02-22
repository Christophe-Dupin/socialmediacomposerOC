from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from .models import SocialMedia
from .forms import PostForm


def login(request):
    return render(request, "login.html")


@login_required
def home(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if not form.is_valid():
            return render(request, "posts/home.html", {"form": form})
        post = Post(
            body=form.cleaned_data["body"],
            author=request.user,
        )
        post.save()
        for x in form.cleaned_data["socialmedia"]:
            post.socialmedia.add(x.id)
            # post.post_on_Linkedin()
            # post.post_on_facebook()

    form = PostForm()
    return render(request, "posts/home.html", {"form": form})


@login_required
def all_posts_queue(request):
    context = Post.get_all_post_on_queue()
    return render(request, "posts/posts_queue.html", {"context": context})


@login_required
def all_posts_send(request):
    context = Post.get_all_post_history()
    return render(request, "posts/posts_history.html", {"context": context})
