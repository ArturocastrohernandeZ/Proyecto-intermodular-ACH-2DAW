
import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR.parent / ".env")

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "").strip()
if not SECRET_KEY:
    raise ImproperlyConfigured("Falta DJANGO_SECRET_KEY. Ejecuta python backend/configure_env.py.")

DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
    if host.strip()
]

ROOT_URLCONF = "config.urls"
INSTALLED_APPS = []
MIDDLEWARE = []

LANGUAGE_CODE = "es"
TIME_ZONE = "Europe/Madrid"
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
