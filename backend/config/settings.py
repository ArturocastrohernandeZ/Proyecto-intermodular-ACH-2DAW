
import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-solo-desarrollo-local")
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

ROOT_URLCONF = "config.urls"
INSTALLED_APPS = []
MIDDLEWARE = []
