from django.shortcuts import render

from .models import Usuario,Departament


# Create your views here.
def index(request):
    usuarios=Usuario.ob