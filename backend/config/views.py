from django.http import HttpResponse


def hola_mundo(request):
  
    return HttpResponse("hola mundo", content_type="text/plain; charset=utf-8")
