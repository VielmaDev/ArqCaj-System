
from django.db import models
from tabnanny import verbose
from ProyectoWebAC.models import tienda # importando tabla tienda
from ArqueoCaja.models import arqueo # importando tabla arqueo
from django.utils import timezone

# Create your models here.

class inventario_ventas(models.Model):

    tienda=models.ForeignKey(tienda, on_delete=models.CASCADE)
    arqueo=models.ForeignKey(arqueo, on_delete=models.CASCADE)

    calzados=models.CharField(max_length=5, null=False)
    ropa=models.CharField(max_length=5, null=False)
    accesorios=models.CharField(max_length=5, null=False)
    piezas=models.CharField(max_length=10, null=False)
    procesado=models.BooleanField(default=False)

    created=models.DateField()
    update=models.DateField(auto_now_add=True)
    

    class Meta:

        verbose_name= "Inventario"
        verbose_name_plural="Inventarios"

    def __str__(self):

         return self.tienda_id