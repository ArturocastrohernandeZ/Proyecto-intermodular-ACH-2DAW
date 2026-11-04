from django.apps import AppConfig


# UD3.2f: configuración de la app core.
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = "Clases"