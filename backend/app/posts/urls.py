from django.urls import path

from . import views

urlpatterns = [
    path("add_post/", views.add_post, name="add_post"),
    path(
        "all_posts_queue/",
        views.all_posts_queue,
        name="all_posts_queue",
    ),
    path(
        "all_posts_queue_linkedin/",
        views.all_posts_queue_linkedin,
        name="all_posts_queue_linkedin",
    ),
    path(
        "all_posts_queue_facebook/",
        views.all_posts_queue_facebook,
        name="all_posts_queue_facebook",
    ),
    path("queue/", views.all_posts_queue, name="all_posts_queue"),
    path("history/", views.all_posts_send, name="all_posts_send"),
    path(
        "delete_a_selected_post/<int:id>",
        views.delete_a_selected_post,
        name="delete_a_selected_post",
    ),
    path(
        "delete_a_linkedin_selected_post/<int:id>",
        views.delete_a_linkedin_selected_post,
        name="delete_a_linkedin_selected_post",
    ),
    path(
        "delete_a_facebook_selected_post/<int:id>",
        views.delete_a_facebook_selected_post,
        name="delete_a_facebook_selected_post",
    ),
    path(
        "share_now_a_linkedin_post/<int:id>",
        views.share_now_a_linkedin_post,
        name="share_now_a_linkedin_post",
    ),
    path(
        "manage_my_channels/",
        views.manage_my_channels,
        name="manage_my_channels",
    ),
]
