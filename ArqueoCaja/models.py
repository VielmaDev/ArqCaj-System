
from django.db import models
from tabnanny import verbose
from ProyectoWebAC.models import tienda, caja, tasaDivisa #Importando tabla de la App ProyectoWebAC

# Create your models here.
    
class arqueo(models.Model):

    tienda=models.ForeignKey(tienda, on_delete=models.CASCADE)
    caja=models.ForeignKey(caja, on_delete=models.CASCADE)
    tasaDivisa=models.ForeignKey(tasaDivisa, on_delete=models.CASCADE)
    
    ef_bs=models.CharField(max_length=10, null=False)
    ef_usd=models.CharField(max_length=10, null=False)
    ef_eur=models.CharField(max_length=10, null=False)

    td_bs=models.CharField(max_length=10, null=False)
    tc_usd=models.CharField(max_length=10, null=False)
    tc_bs=models.CharField(max_length=10, null=False)

    tr_bs=models.CharField(max_length=10, null=False)
    tr_zll=models.CharField(max_length=10, null=False)
    pm_bs=models.CharField(max_length=10, null=False)
   
    ti_bs=models.CharField(max_length=20, null=False)
    ti_usd=models.CharField(max_length=20, null=False)
    ti_eur=models.CharField(max_length=20, null=False)
    ti_zll=models.CharField(max_length=20, null=False)

    vn_usd=models.CharField(max_length=40, null=False)
    vn_bs=models.CharField(max_length=40, null=False)


    fi=models.CharField(max_length=10, null=False)
    gt=models.CharField(max_length=10, null=False)
    dt=models.CharField(max_length=10, null=False)
    dv=models.CharField(max_length=10, null=False)
    
    df=models.CharField(max_length=10, null=False)
    cierre=models.CharField(max_length=30, null=False)
    nota=models.CharField(max_length=250, null=True)

    procesado=models.BooleanField()

    created=models.CharField(max_length=10, null=False)
    update=models.DateField(auto_now_add=True)
    
    class Meta:

        verbose_name= "Arqueo"
        verbose_name_plural="Arqueos"

    def __str__(self):

        return self.tienda
