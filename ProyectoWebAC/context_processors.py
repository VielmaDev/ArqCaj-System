
#importación de la función render
from django.shortcuts import render

#Importación de tabla tienda
from .models import tienda, caja, tasaDivisa, comunicado

#Importar zona horaria
from datetime import date, datetime

def tiendaView(request):

    #Carga datos de la tienda del usuario logeado
    tiendaset= tienda.objects.filter(user=(1))

    #para generar los reportes de cierre de todas las tiendas
    tiendaall=tienda.objects.all()
    
    return {'tiendaset': tiendaset, 'tiendaall':tiendaall}

def cajaView(request):

    cajaset= caja.objects.filter(tienda=(1))
    return {'cajaset': cajaset}

def divisaView(request):

    divisaset= tasaDivisa.objects.filter(id=(1))
    return {'divisaset': divisaset}

def notaView(request):

    notaset= comunicado.objects.all()
    return {'notaset': notaset}
