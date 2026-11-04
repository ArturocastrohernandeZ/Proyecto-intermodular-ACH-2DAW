from django.views.generic import TemplateView


# UD3.7a: muestra el panel enlazado desde la plantilla base.
class PanelView(TemplateView):
    template_name = "common/panel.html"
