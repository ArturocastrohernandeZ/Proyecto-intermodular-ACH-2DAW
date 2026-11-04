from django.contrib import admin
from .models import Cliente, Cobro, Factura
# Register your models here.

# UD3.4b: administración de clientes
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellidos", "nif", "email") #columnas listado
    list_display_links = list_display #Columnas que abren el cliente 
    list_filter = ("nif",) #Filtro por nif
    search_fields = ("nombre", "apellidos", "nif", "email") #Campos por los que puedes buscar
    preserve_filters = True #Mantiene los filtros al volver 

# UD3.4b: administración de facturas
@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ("numero_factura", "fecha", "total") #Columnas listado
    list_display_links = list_display # Columnas que abren la factura 
    list_filter = ("cliente",)#Filtro por cliente
    search_fields = ("numero_factura", "cliente__nombre", "cliente__apellidos")#Busca por factura y por nombre del cliente
    preserve_filters = True #Mantiene los filtros 

# UD3.4b: administración de cobros.
@admin.register(Cobro)
class CobroAdmin(admin.ModelAdmin):
    list_display = ("numero_factura", "fecha", "importe")  # Columnas del listado.
    list_display_links = list_display  # Columnas que abren el cobro.
    list_filter = ("factura__cliente",)  # Filtra por el cliente de la factura.
    search_fields = ("factura__numero_factura","factura__cliente__nombre","factura__cliente__apellidos",)  # Busca datos de la factura y su cliente.
    preserve_filters = True  # Mantiene los filtros al volver al listado.

    @admin.display(description="N.º factura", ordering="factura__numero_factura")
    def numero_factura(self, obj):
        return obj.factura.numero_factura
