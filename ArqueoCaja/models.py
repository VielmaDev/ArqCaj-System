
from django.db import models
from tabnanny import verbose
from ProyectoWebAC.models import tienda, tasa, caja #Importando tabla de la App ProyectoWebAC
from django.utils import timezone

# Create your models here.

class ingresos(models.Model):

    tienda_id=models.ForeignKey(tienda, on_delete=models.CASCADE)
    caja_id=models.ForeignKey(caja, on_delete=models.CASCADE)
    tasa_id=models.ForeignKey(tasa, on_delete=models.CASCADE)

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

    created=models.DateField()
    update=models.DateField(auto_now_add=True)
    
    class Meta:

        verbose_name= "Ingreso"
        verbose_name_plural="Ingresos"

    def __str__(self):

         return self.tienda_id
    
class arqueo(models.Model):

    tienda_id=models.ForeignKey(tienda, on_delete=models.CASCADE)
    caja_id=models.ForeignKey(caja, on_delete=models.CASCADE)
    ingreso_id=models.ForeignKey(ingresos, on_delete=models.CASCADE)

    cii=models.CharField(max_length=30, null=False)
    sg=models.CharField(max_length=30, null=False)
    dt=models.CharField(max_length=30, null=False)
    cif=models.CharField(max_length=30, null=False)
    vd=models.CharField(max_length=30, null=False)
    ft=models.CharField(max_length=30, null=False)
    st=models.CharField(max_length=30, null=False)
    nota=models.CharField(max_length=120, null=False)
    procesado=models.BooleanField(default=False)

    created=models.DateField()
    update=models.DateField(auto_now_add=True)
    
    class Meta:

        verbose_name= "Arqueo"
        verbose_name_plural="Arqueos"

    def __str__(self):

        return self.tienda_id
