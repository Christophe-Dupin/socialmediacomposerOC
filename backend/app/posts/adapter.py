from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from app.users.models import User


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if user.id:
            return
        try:
            existing_user = User.objects.get(email=user.email)
            sociallogin.state["process"] = "connect"
            perform_login(request, existing_user, "none")
        except User.DoesNotExist:
            pass
