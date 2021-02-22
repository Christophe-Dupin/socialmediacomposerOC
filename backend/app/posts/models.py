from django.db import models
from app.users.models import User
import os
import requests


class SocialMedia(models.Model):
    socialmedia = models.CharField(max_length=255)

    def __str__(self):
        return self.socialmedia


class Post(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    schedule_time = models.DateTimeField()
    is_queue = models.BooleanField(default=True)
    is_send = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    socialmedia = models.ManyToManyField(SocialMedia)

    def post_on_Linkedin(self):
        api_url = "https://api.linkedin.com/v2/ugcPosts"
        user = User.objects.get(username=self.author)
        social = user.social_auth.get(provider="linkedin-oauth2")
        access_token = social.extra_data["access_token"]
        headers = {
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        urn = social.extra_data["id"]
        author = f"urn:li:person:{urn}"
        post_data = {
            "author": author,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": self.body},
                    "shareMediaCategory": "NONE",
                },
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "CONNECTIONS"
            },
        }
        response = requests.post(api_url, headers=headers, json=post_data)

        if response.status_code == 201:
            print("Success")
        print(response.content)

    def post_on_facebook(self):
        user = User.objects.get(username="cdupin")
        social = user.social_auth.get(provider="facebook")
        id = social.extra_data["id"]
        access_token = social.extra_data["access_token"]
        api_url = f"https://graph.facebook.com/{id}/feed"
        headers = {
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        post_data = {
            "published": "true",
            "message": {"text": self.body},
            "access_token": access_token,
        }
        response = requests.post(api_url, headers=headers, json=post_data)

        if response.status_code == 201:
            print("Success")
        print(response.content)

    def get_all_post_on_queue():
        return Post.objects.filter(is_queue=True)

    def get_all_post_history():
        return Post.objects.filter(is_send=True)

    def get_all_post_on_queue_by_social_media(socialmedia):
        return Post.objects.filter(is_queue=True, socialmedia=socialmedia)

    def delete_a_selected_post(pk):
        return Post.objects.filter(id=pk).delete()

    def edit_a_selected_post(pk):
        return Post.objects.filter(id=pk)
