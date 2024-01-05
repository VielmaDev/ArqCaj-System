
from django.db import models
from tabnanny import verbose
from ProyectoWebAC.models import tienda, tasaDolar, caja #Importando tabla de la App ProyectoWebAC
from django.utils import timezone

# Create your models here.

class ventas(models.Model):

    tienda_id=models.ForeignKey(tienda, on_delete=models.CASCADE)
    caja_id=models.ForeignKey(caja, on_delete=models.CASCADE)
    tasaDolar=models.ForeignKey(tasaDolar, on_delete=models.CASCADE)

    ef_bs=models.CharField(max_length=10, null=False)
    td_bs=models.CharField(max_length=10, null=False)
    tc_bs=models.CharField(max_length=10, null=False)
    pm_bs=models.CharField(max_length=10, null=False)
    nc_bs=models.CharField(max_length=10, null=False)
    ti_bs=models.CharField(max_length=20, null=False)

    ef_usd=models.CharField(max_length=10, null=False)
    tc_usd=models.CharField(max_length=10, null=False)
    td_usd=models.CharField(max_length=10, null=False)
    pm_usd=models.CharField(max_length=10, null=False)
    nc_usd=models.CharField(max_length=10, null=False)
    ti_usd=models.CharField(max_length=20, null=False)
    conversion_usd=models.CharField(max_length=20, null=False)

    nota=models.CharField(max_length=300, null=False)

    tif=models.CharField(max_length=30, null=False)

    procesado=models.BooleanField()

    created=models.DateField()
    update=models.DateField(auto_now_add=True)
    
    class Meta:

        verbose_name= "Ingreso"
        verbose_name_plural="Ingresos"

    def __str__(self):

         return self.tienda_id
    
