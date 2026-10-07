from django.http import HttpResponse, JsonResponse


def hola_mundo(request):
  
    return HttpResponse("hola mundo", content_type="text/plain; charset=utf-8")


def health(request):
    """Endpoint de prueba para comprobar la comunicación con el frontend."""
    return JsonResponse({"status": "ok"})
