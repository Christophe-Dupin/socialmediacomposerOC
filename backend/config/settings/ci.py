
import os
from .base import *  # noqa: F401, F403
SECRET_KEY = os.getenv('SECRET_KEY', default="Cu96ky2qXk9yxxd4CrDOlQpFrCTJNl31sxtxBhEfpVBDxe6SGOlkUUuFT7nqk654")
ALLOWED_HOSTS = ["*"]
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        'HOST': "postgres",
        "PORT": "5432",
    }
}
