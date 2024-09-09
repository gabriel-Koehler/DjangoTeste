from datetime import datetime

from django.db import models


# Create your models here.
class Usuario(models.Model):
    nome:models.CharField(max_length=100)
    password:models.CharField(max_length=255)
    email:models.CharField(unique=True)
    create_on: models.DateTimeField(default=datetime.now())

    def __str__(self): return f'{self.email}'

class Departament(models.Model):
    name:models.CharField()
    usuario:models.ForeignKey(Usuario,on_delete=models.CASCADE)
    create_on:models.DateTimeField(default=datetime.now())

    def __str__(self): return f'{self.name}'