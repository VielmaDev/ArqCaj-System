
from django.db import models
from tabnanny import verbose
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class inventario_ventas(models.Model):

    calzados=models.IntegerField(max_length=4)
    ropa=models.IntegerField(max_length=4)
    accesorios=models.IntegerField(max_length=4)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)

class Meta:

    verbose_name= "Inventario"
    verbose_name_plural="Inventarios"

    def __str__(self):

        return self.calzados