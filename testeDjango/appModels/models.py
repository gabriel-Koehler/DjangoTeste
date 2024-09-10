from datetime import datetime

from django.db import models


# Create your models here.
class Usuario(models.Model):
    name=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=255,null=True)
    email=models.EmailField(unique=True,null=True)
    create_on= models.DateTimeField(default=datetime.now())

    def __str__(self): return self.email

class Departament(models.Model):
    name=models.CharField(max_length=100,null=True)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True )
    create_on=models.DateTimeField(default=datetime.now(),null=True)

    def __str__(self): return self.name