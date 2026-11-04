from django.urls import path

from .views import (
    ActividadDetailView,
    ActividadListView,
    CategoriaDetailView,
    CategoriaListView,
    ProfesorDetailView,
    ProfesorListView,
    ReservaDetailView,
    ReservaListView,
    SesionClaseDetailView,
    SesionClaseListView,
)

app_name = "core"

urlpatterns = [
    # UD3.7b: rutas de lista y detalle de actividades.
    path("actividades/", ActividadListView.as_view(), name="actividad_list"),
    path("actividades/<int:pk>/", ActividadDetailView.as_view(), name="actividad_detail"),
    # UD3.7b: rutas de lista y detalle de categorías.
    path("categorias/", CategoriaListView.as_view(), name="categoria_list"),
    path("categorias/<int:pk>/", CategoriaDetailView.as_view(), name="categoria_detail"),
    # UD3.7b: rutas de lista y detalle de profesores.
    path("profesores/", ProfesorListView.as_view(), name="profesor_list"),
    path("profesores/<int:pk>/", ProfesorDetailView.as_view(), name="profesor_detail"),
    # UD3.7b: rutas de lista y detalle de sesiones de clase.
    path("sesiones/", SesionClaseListView.as_view(), name="sesionclase_list"),
    path("sesiones/<int:pk>/", SesionClaseDetailView.as_view(), name="sesionclase_detail"),
    # UD3.7b: rutas de lista y detalle de reservas.
    path("reservas/", ReservaListView.as_view(), name="reserva_list"),
    path("reservas/<int:pk>/", ReservaDetailView.as_view(), name="reserva_detail"),
]
