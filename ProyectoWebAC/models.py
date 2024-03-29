
from django.db import models
from tabnanny import verbose
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class tienda(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    codigo_tienda=models.CharField(max_length=6, null=False)
    razon=models.CharField(max_length=30, null=False)
    rif= models.CharField(max_length=12, null=False)
    nif= models.CharField(max_length=12, null=False)
    direccion= models.CharField(max_length=25, null=False)
    telf=models.CharField(max_length=30, null=True)
    redes=models.CharField(max_length=25, null=True)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)   
      
    class Meta:

        verbose_name="Tienda"
        verbose_name_plural="Tiendas"

    def __str__(self):

        return self.codigo_tienda

class caja(models.Model):

    tienda=models.ForeignKey(tienda, on_delete=models.CASCADE)
    codigo_caja=models.CharField(max_length=4, null=False)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name= "Caja"
        verbose_name_plural="Cajas"

    def __str__(self):

        return self.codigo_caja

class tasaDivisa(models.Model):

    tasa_usd=models.CharField(max_length=6, null=False)
    tasa_eur=models.CharField(max_length=6, null=False)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="Divisa"
        verbose_name_plural="Divisas"

    def __str__(self):

        return self.created

    
class comunicado(models.Model):

    nota= models.CharField(max_length=200, null=False)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="Nota"
        verbose_name_plural="Notas"

    def __str__(self):

        return self.nota