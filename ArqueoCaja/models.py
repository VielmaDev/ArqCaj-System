
from django.db import models
from tabnanny import verbose
from ProyectoWebAC.models import tienda, caja #Importando tabla de la App ProyectoWebAC
from django.utils import timezone

# Create your models here.
    
class arqueo(models.Model):

    tienda_id=models.ForeignKey(tienda, on_delete=models.CASCADE)
    caja_id=models.ForeignKey(caja, on_delete=models.CASCADE)
   
    cii=models.CharField(max_length=30, null=False)
    sg=models.CharField(max_length=30, null=False)
    dt=models.CharField(max_length=30, null=False)
    cif=models.CharField(max_length=30, null=False)
    vd=models.CharField(max_length=30, null=False)
    ft=models.CharField(max_length=30, null=False)
    st=models.CharField(max_length=30, null=False)
    nota=models.CharField(max_length=120, null=False)
    procesado=models.BooleanField()

    created=models.DateField()
    update=models.DateField(auto_now_add=True)
    
    class Meta:

        verbose_name= "Arqueo"
        verbose_name_plural="Arqueos"

    def __str__(self):

        return self.tienda_id
