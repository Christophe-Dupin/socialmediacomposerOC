from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("queue/", views.all_posts_queue, name="all_posts_queue"),
    path("history/", views.all_posts_send, name="all_posts_send"),
]
