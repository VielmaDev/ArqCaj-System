
from django.db import models
from tabnanny import verbose
from ProyectoWebAC.models import tienda, caja, tasaDolar, tasaEuro #Importando tabla de la App ProyectoWebAC
from django.utils import timezone

# Create your models here.
    
class arqueo(models.Model):

    tienda=models.ForeignKey(tienda, on_delete=models.CASCADE)
    caja=models.ForeignKey(caja, on_delete=models.CASCADE)
    tasaDolar=models.ForeignKey(tasaDolar, on_delete=models.CASCADE)
    tasaEuro=models.ForeignKey(tasaEuro, on_delete=models.CASCADE)

    
    ef_bs=models.CharField(max_length=10, null=False)
    ef_usd=models.CharField(max_length=10, null=False)
    ef_eur=models.CharField(max_length=10, null=False)

    td_bs=models.CharField(max_length=10, null=False)
    td_usd=models.CharField(max_length=10, null=False)
    tc_bs=models.CharField(max_length=10, null=False)

    tr_bs=models.CharField(max_length=10, null=False)
    tr_zll=models.CharField(max_length=10, null=False)
    pm_bs=models.CharField(max_length=10, null=False)
   
    ti_bs=models.CharField(max_length=20, null=False)
    ti_usd=models.CharField(max_length=20, null=False)
    ti_eur=models.CharField(max_length=20, null=False)
    ti_zll=models.CharField(max_length=20, null=False)
    ti=models.CharField(max_length=30, null=False)

    sg=models.CharField(max_length=30, null=False)
    dt=models.CharField(max_length=30, null=False)
    dv=models.CharField(max_length=30, null=False)
    
    ft=models.CharField(max_length=30, null=False)
    st=models.CharField(max_length=30, null=False)
    cierre=models.CharField(max_length=30, null=False)
    nota=models.CharField(max_length=120, null=False)

    procesado=models.BooleanField()
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)
    
    class Meta:

        verbose_name= "Arqueo"
        verbose_name_plural="Arqueos"

    def __str__(self):

        return self.tienda_id
