from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from .models import Post
from app.users.models import User
from .forms import PostForm


def login(request):
    return render(request, "login.html")


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if not form.is_valid():
            print("tutu")
            return render(request, "posts/home.html", {"form": form})
        post = Post(
            body=form.cleaned_data["body"],
            schedule_time=form.cleaned_data["schedule_time"],
            author=request.user,
        )
        post.save()
        for x in form.cleaned_data["socialmedia"]:
            post.socialmedia.add(x.id)
            # post.post_on_Linkedin()
            # post.post_on_facebook()
    form = PostForm()
    social_account = SocialAccount.objects.filter(user=request.user)
    print(social_account)
    for x in social_account:
        print(x)
    return render(
        request,
        "posts/home.html",
        {"form": form, "social_Account": social_account},
    )


@login_required
def all_posts_queue(request):
    post = Post.objects.get_all_post_on_queue()
    print(post)
    return render(
        request,
        "posts/posts_queue.html",
        {"post": post},
    )


@login_required
def all_posts_queue_linkedin(request):
    context = Post.objects.filter(
        socialmedia__socialmedia__startswith="linkedin", is_queue=True
    )
    return render(
        request, "posts/posts_linkedin_queue.html", {"context": context}
    )


@login_required
def all_posts_queue_facebook(request):
    context = Post.objects.filter(
        socialmedia__socialmedia__startswith="facebook", is_queue=True
    )
    return render(
        request, "posts/posts_facebook_queue.html", {"context": context}
    )


@login_required
def all_posts_send(request):
    context = Post.objects.get_all_post_history()
    return render(request, "posts/posts_history.html", {"context": context})


@login_required
def delete_a_selected_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("all_posts_queue")


@login_required
def delete_a_linkedin_selected_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("all_posts_queue_linkedin")


@login_required
def delete_a_facebook_selected_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("all_posts_queue_facebook")


@login_required
def share_now_a_linkedin_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.post_on_Linkedin()
    post.is_queue = False
    post.is_send = True
    post.save()
    return redirect("all_posts_queue_linkedin")


@login_required
def manage_my_channels(request):
    user = request.user
    social = user.social_auth.get()
    context = social.provider
    return render(request, "posts/manage_channels.html", {"context": context})
