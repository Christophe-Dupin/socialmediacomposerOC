from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post
from app.users.models import User
from .forms import PostForm


def login(request):
    """Login view

    :param request: http request object
    :type request: request
    :return: Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
    :rtype: HttpResponse
    """
    return render(request, "login.html")


def help(request):
    """Help view: give help contact to the user

    :param request: http request object
    :type request: Request
    :return: Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
    :rtype: HttpResponse
    """
    return render(request, "posts/help.html")


@login_required
def add_post(request):
    """Allow user to add post, he has to choose a social media and define a schedule time.

    :param request: request object
    :type request: Request
    :return: Combine un gabarit donné avec un dictionnaire contexte contenant le formulaire et renvoie un objet HttpResponse avec le texte résultant.
    :rtype: HttpResponse
    """
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
    return render(request, "posts/home.html", {"form": form})


@login_required
def all_posts_queue(request):
    """Allow to display all the post on queue for all the social media.

    :param request:  http request object
    :type request: Request
    :return: Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
    :rtype: HttpResponse
    """
    post = Post.objects.get_all_post_on_queue(request.user)
    return render(
        request,
        "posts/posts_queue.html",
        {"post": post},
    )


@login_required
def all_posts_queue_linkedin(request):
    """Allow to display all the post on queue only for linkedin

    :param request: http request object
    :type request: Request
    :return:Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
    :rtype: HttpResponse
    """
    context = Post.objects.filter(
        socialmedia__socialmedia__startswith="linkedin",
        is_queue=True,
        author=request.user,
    )
    return render(
        request, "posts/posts_linkedin_queue.html", {"context": context}
    )


@login_required
def all_posts_queue_facebook(request, author):
    """Allow to display all the post on queue only for facebook

    :param request: http request object
    :type request: Request
    :param author: the author of the post
    :type author: User
    :return: Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text
    :rtype: HttpResponse
    """
    context = Post.objects.filter(
        socialmedia__socialmedia__startswith="facebook",
        is_queue=True,
        author=request.user,
    )
    return render(
        request, "posts/posts_facebook_queue.html", {"context": context}
    )


@login_required
def all_posts_send(request):
    """Allow to display all the post send by a user

    :param request: Request object
    :type request: Request
    :return: Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text
    :rtype: HttpResponse
    """
    context = Post.objects.get_all_post_history(
        request.user,
    )
    return render(request, "posts/posts_history.html", {"context": context})


@login_required
def delete_a_selected_post(request, id):
    """Allow to delete a post depends to the id.

    :param request: request object
    :type request: Request
    :param id: the id of the authenticated user
    :type id: int
    :return: Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text
    :rtype: HttpResponse
    """
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("all_posts_queue_linkedin")


@login_required
def delete_a_linkedin_selected_post(request, id):
    """Allow to delete a linkedin post depends to the id.


    :param request: request object
    :type request: Request
    :param id: the id of the authenticated user
    :type id: int
    :return: Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text
    :rtype: HttpResponse
    """
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("all_posts_queue_linkedin")


@login_required
def delete_a_facebook_selected_post(request, id):
    """Allow to delete a facebook post depends to the id.


    :param request: request object
    :type request: Request
    :param id: the id of the authenticated user
    :type id: int
    :return: Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text
    :rtype: HttpResponse
    """
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("all_posts_queue_facebook")


@login_required
def share_now_a_linkedin_post(request, id):
    """Allow user to share rigth now any post.

    :param request: request object
    :type request: Request
    :param id: id of the selected post
    :type id: int
    :return: Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text
    :rtype: HttpResponse
    """
    post = get_object_or_404(Post, id=id)
    post.post_on_Linkedin()
    post.is_queue = False
    post.is_send = True
    post.save()
    return redirect("all_posts_queue_linkedin")


@login_required
def manage_my_channels(request):
    """Allow user to manage the connected channel

    :param request: request object
    :type request: Request
    :return: Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text
    :rtype: HttpResponse
    """
    user = request.user
    social = user.social_auth.get()
    return render(request, "posts/manage_channels.html", {"social": social})
