from django.views.generic import DetailView, ListView

from .models import Cliente, Cobro, Factura


# UD3.8b: lista paginada de clientes.
class ClienteListView(ListView):
    model = Cliente
    template_name = "billing/cliente_list.html"
    paginate_by = 5


# UD3.8b: detalle enlazado desde la lista de clientes.
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "billing/cliente_detail.html"


# UD3.8b: lista paginada de facturas.
class FacturaListView(ListView):
    model = Factura
    template_name = "billing/factura_list.html"
    paginate_by = 5


# UD3.8b: detalle enlazado desde la lista de facturas.
class FacturaDetailView(DetailView):
    model = Factura
    template_name = "billing/factura_detail.html"


# UD3.8b: lista paginada de cobros.
class CobroListView(ListView):
    model = Cobro
    template_name = "billing/cobro_list.html"
    paginate_by = 5


# UD3.8b: detalle enlazado desde la lista de cobros.
class CobroDetailView(DetailView):
    model = Cobro
    template_name = "billing/cobro_detail.html"
