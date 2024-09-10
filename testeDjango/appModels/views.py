from django.http import HttpResponse
from django.shortcuts import render

from .models import Usuario,Departament

# Create your views here.
def index(request):
    teste=Usuario(name="name",email="email@mail.com",password="password")

    usuarios=Usuario.objects.all().values()
    print(usuarios)

    return  render(request,'index.html')

