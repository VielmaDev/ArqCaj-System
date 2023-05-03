
from tabnanny import verbose
from django.db import models

#from django.contrib.auth.models import User

# Create your models here.

class tienda(models.Model):

    razon=models.CharField(max_length=20)
    rif= models.CharField(max_length=12)
    direccion= models.CharField(max_length=30)
    telf=models.CharField(max_length=30)
    redes=models.CharField(max_length=30)
    n_caja=models.CharField(max_length=2)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    
        
class Meta:

    verbose_name= "Tienda"
    verbose_name_plural="Tiendas"

    def __str__(self):

        return self.razon
    
class divisas(models.Model):

    tasaDolar=models.FloatField()
    tasaEuro=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

class Meta:

    verbose_name= "Divisa"
    verbose_name_plural="Divisas"

    def __str__(self):

        return self.tasa_dolar






