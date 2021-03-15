from django.core.management.base import BaseCommand
from datetime import datetime
from app.posts.models import Post


class Command(BaseCommand):
    """Add specifique commande to manage.py
    :param BaseCommand: Legacy from BaseCommand class
    :type BaseCommand: BaseCommand
    """

    help = "Post linkedin publish"

    def handle(self, *args, **options):
        """Methode to launch the specifque commande."""
        all_post = Post.objects.get_all_post_on_queue()
        for post in all_post:
            if post.schedule_time <= datetime.now():
                post.post_on_Linkedin()
