from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("profile/", views.profile, name="profile"),
    path("activate/<uidb64>", views.activate, name="activate"),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="users/password_reset.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_send/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
    path("manage_channels/", views.manage_channels, name="manage_channels"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
]
