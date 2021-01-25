from django.urls import path

from . import views

urlpatterns = [
    path("queue/", views.all_posts_queue, name="all_posts"),
    path("history/", views.all_posts_send, name="all_posts_send"),
]
