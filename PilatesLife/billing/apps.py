from django.apps import AppConfig


# UD3.2f: configuración de la app billing.
class BillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'billing'
    verbose_name = "Facturación"