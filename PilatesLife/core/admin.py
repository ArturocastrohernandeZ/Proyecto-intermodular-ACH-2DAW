from django.contrib import admin
from .models import Profesor, Categoria, Actividad, SesionClase, Reserva, Notificacion


# UD3.4c: administración de profesores.
@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellidos", "usuario", "especialidad")  # Columnas.
    list_filter = ("especialidad",)  # Filtro por especialidad.
    search_fields = ("nombre", "apellidos", "usuario__username")  # Búsqueda.


# UD3.4c: administración de categorías.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria_padre")  # Columnas.
    list_filter = ("categoria_padre",)  # Filtro por categoría superior.
    search_fields = ("nombre", "descripcion")  # Búsqueda.


# UD3.4c: administración de actividades.
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "duracion_minutos", "precio_base")  # Columnas.
    list_filter = ("categoria",)  # Filtro por categoría.
    search_fields = ("nombre", "descripcion")  # Búsqueda.


# UD3.4c: administración de sesiones.
@admin.register(SesionClase)
class SesionClaseAdmin(admin.ModelAdmin):
    list_display = ("actividad", "profesor", "fecha_inicio", "aforo", "estado")  # Columnas.
    list_filter = ("estado", "profesor")  # Filtros de sesiones.
    search_fields = ("actividad__nombre", "profesor__apellidos")  # Búsqueda.


# UD3.4c: administración de reservas.
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "sesion", "fecha_creacion", "estado")  # Columnas.
    list_filter = ("estado",)  # Filtro por estado.
    search_fields = ("cliente__nombre", "cliente__apellidos")  # Búsqueda.


# UD3.4c: administración de notificaciones.
@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ("cliente", "asunto", "canal", "fecha_programada", "estado")  # Columnas.
    list_filter = ("canal", "estado")  # Filtros de notificaciones.
    search_fields = ("asunto", "cliente__nombre", "cliente__apellidos")  # Búsqueda.