from django.contrib import admin

# Register your models here.
from .models import Usuario,Departament

admin.site.register(Usuario)
admin.site.register(Departament)
