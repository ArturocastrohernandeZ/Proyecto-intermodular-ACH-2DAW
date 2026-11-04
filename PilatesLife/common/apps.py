from django.apps import AppConfig


# UD3.2f: configuración de la app common.
class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common'
    verbose_name = "Común"