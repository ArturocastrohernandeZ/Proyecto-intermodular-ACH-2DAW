from django.urls import path

from .views import health, hola_mundo

urlpatterns = [
    path("", hola_mundo, name="hola_mundo"),
    path("api/health/", health, name="health"),
]
