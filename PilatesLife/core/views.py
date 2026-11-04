from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView, ListView

from .models import Actividad, Categoria, Profesor, Reserva, SesionClase


# UD3.7a: muestra la lista de actividades.
class ActividadListView(ListView):
    model = Actividad
    template_name = "core/actividad_list.html"
    # UD3.8b: muestra cinco actividades por página.
    paginate_by = 5


# UD3.7a: muestra el detalle de una actividad.
class ActividadDetailView(DetailView):
    model = Actividad
    template_name = "core/actividad_detail.html"


# UD3.7a: muestra la lista de categorías.
class CategoriaListView(ListView):
    model = Categoria
    template_name = "core/categoria_list.html"
    # UD3.8b: muestra cinco categorías por página.
    paginate_by = 5


# UD3.7a: muestra el detalle de una categoría.
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = "core/categoria_detail.html"


# UD3.7a: muestra la lista de profesores.
class ProfesorListView(ListView):
    model = Profesor
    template_name = "core/profesor_list.html"
    # UD3.8b: muestra cinco profesores por página.
    paginate_by = 5


# UD3.7a: muestra el detalle de un profesor.
class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = "core/profesor_detail.html"


# UD3.7a: muestra la lista de sesiones de clase.
class SesionClaseListView(ListView):
    model = SesionClase
    template_name = "core/sesionclase_list.html"
    # UD3.8b: muestra cinco sesiones por página.
    paginate_by = 5


# UD3.7a: muestra el detalle de una sesión de clase.
class SesionClaseDetailView(DetailView):
    model = SesionClase
    template_name = "core/sesionclase_detail.html"


# UD3.7a: muestra las reservas a usuarios con permiso.
class ReservaListView(PermissionRequiredMixin, ListView):
    permission_required = "core.view_reserva"
    raise_exception = True
    model = Reserva
    template_name = "core/reserva_list.html"
    # UD3.8b: muestra cinco reservas por página.
    paginate_by = 5


# UD3.7a: muestra una reserva a usuarios con permiso.
class ReservaDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "core.view_reserva"
    raise_exception = True
    model = Reserva
    template_name = "core/reserva_detail.html"
