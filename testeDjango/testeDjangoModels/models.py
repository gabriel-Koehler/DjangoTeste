from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome:models.CharField(max_length=100)
    password:models.CharField(max_length=255)
    email:models.CharField(unique=True)
class Departament(models.Model):
    name:models.CharField()
    usuario:models.ForeignKey(Usuario,on_delete=models.CASCADE)
