#importación de la función render
from django.shortcuts import render

#Importación de tabla tienda
from .models import arqueo

def arqueoView(request):

    arqueoset= arqueo.objects.filter(tienda=(1))
    #arqueoset= arqueo.objects.all()
    return {'arqueoset': arqueoset}