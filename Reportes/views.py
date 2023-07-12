
#Importación de librería de vistas
from django.views.generic import ListView, DetailView 

#Libreria para mensajes
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

#Importación de librería retorno
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse

#Importación de las DB de la app Ingresos y ArqueoCaja
from Ingresos.models import ventas
from ArqueoCaja.models import arqueo


#Para obtener todos los campos de un registro de la tabla arqueo
class ListaIngresos(DetailView): 
    model = ventas

# Realizar busqueda por parametros        
def buscar(request):

    if request.GET["fecha"]:
        Fecha= request.GET["fecha"]

        Ventas= ventas.objects.filter(created__icontains= Fecha)
        return render(request, "Reportes/dia.html", {"Ventas": Ventas})
        
    #else:
        #success_message = 'No se encontraron registros de ventas asociados'

