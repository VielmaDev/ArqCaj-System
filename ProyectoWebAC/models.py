
from django.db import models
from tabnanny import verbose
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class tienda(models.Model):

    razon=models.CharField(max_length=30, null=False)
    rif= models.CharField(max_length=12, null=False)
    direccion= models.CharField(max_length=25, null=False)
    telf=models.CharField(max_length=30, null=True)
    redes=models.CharField(max_length=25, null=True)
    
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)   
      
    class Meta:

        verbose_name="Tienda"
        verbose_name_plural="Tiendas"

    def __str__(self):

        return self.razon

class caja(models.Model):

    tienda_id=models.ForeignKey(tienda, on_delete=models.CASCADE)
    codigo_caja=models.CharField(max_length=4, null=False)

    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    class Meta:

        verbose_name= "Caja"
        verbose_name_plural="Cajas"

    def __str__(self):

        return self.codigo_caja

class tasa(models.Model):

    Dolar=models.CharField(max_length=4, null=False)
    Euro=models.CharField(max_length=4, null=False)
    
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Divisa"
        verbose_name_plural="Divisas"

    def __str__(self):

        return self.Dolar