from django.core.management.base import BaseCommand

from app.posts.models import Post


class Command(BaseCommand):
    """Add specifique commande to manage.py
    :param BaseCommand: Legacy from BaseCommand class
    :type BaseCommand: BaseCommand
    """

    help = "Clean all Product from the db"

    def handle(self, *args, **options):
        """Methode to launch the specifque commande."""
        all_post = Post.objects.get_all_post_on_queue()
        for x in all_post:
            print(x.schedule_time)
