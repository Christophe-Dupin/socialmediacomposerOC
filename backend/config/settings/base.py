"""
Base settings to build other settings files upon.
"""
from pathlib import Path
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = "UTC"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id

# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"


# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPS = [
    "django.contrib.sites",
    "crispy_forms",
    "bootstrap_datepicker_plus",
    "social_django",
    "bootstrap4",
]
LOCAL_APPS = ["app.posts", "app.users"]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# MIDDLEWARE
# ------------------------------------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]
AUTHENTICATION_BACKENDS = [
    "social_core.backends.linkedin.LinkedinOAuth2",
    "social_core.backends.instagram.InstagramOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]
WSGI_APPLICATION = "config.wsgi.application"
# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "app/posts/static"),
    os.path.join(BASE_DIR, "app/users/static"),
]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"
AUTH_USER_MODEL = "users.User"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]
CRISPY_TEMPLATE_PACK = "bootstrap4"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "add_post"
LOGOUT_URL = "logout"
LOGOUT_REDIRECT_URL = "login"
DATE_INPUT_FORMATS = ["%d-%m-%Y"]
# EMAIL SMTP------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# FACEBOOK AUTH------------------------
SOCIAL_AUTH_FACEBOOK_KEY = os.getenv("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv("SOCIAL_AUTH_FACEBOOK_SECRET")
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email", "user_link"]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    "fields": "id, name, email, picture.type(large), link"
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ("name", "name"),
    ("email", "email"),
    ("picture", "picture"),
    ("link", "profile_url"),
]
# LINKEDIN AUTH------------------------
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = "86pddb1z2hflqp"
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = "qiWf2A5G4Tck3kqW"
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "add_post"
SOCIAL_AUTH_LOGIN_URL = "/"
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = [
    "r_liteprofile",
    "r_emailaddress",
    "w_member_social",
]
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = [
    "email-address",
    "formatted-name",
    "public-profile-url",
    "picture-url",
]
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [
    ("id", "id"),
    ("formattedName", "name"),
    ("emailAddress", "email_address"),
    ("pictureUrl", "picture_url"),
    ("publicProfileUrl", "profile_url"),
]
