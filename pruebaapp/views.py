# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo, es mi primera app de prueba en Django soy Jonathan Buri")