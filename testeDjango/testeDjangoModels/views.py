from django.http import HttpResponse
from django.shortcuts import render

from .models import Usuario,Departament

# Create your views here.
def index(request):
    item=Usuario.objects.all()
    Departament.objects
    return HttpResponse("Hello word",item)

