from django.http import HttpResponse
from django.shortcuts import render

from .models import Usuario,Departament

# Create your views here.
def index(request):

    usuarios=Usuario.objects.all().values()
    print(usuarios)
    return  render(request,'index.html')

