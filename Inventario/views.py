
#Consulta de registro
from django.views.generic import ListView, DetailView 

#Creacín y actualización de registro
from django.views.generic.edit import CreateView, UpdateView

#Libreria de retorno
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse

#Libreria para mensajes
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

 # Importando la BD
from .models import inventario_ventas

#Formularios
from django import forms

# Create your views here.

#Para obtener todos los registros de la tabla Inventario_ventas 
class InventarioListar(ListView): 
    model = inventario_ventas
 
#Para obtener todos los campos de un registro de la tabla Inventario_ventas 
class InventarioDetalle(DetailView): 
    model = inventario_ventas
 
#Para insertar un nuevo registro en la tabla Inventario_ventas 
class InventarioNuevo(SuccessMessageMixin, CreateView): 
    model = inventario_ventas
    form = inventario_ventas
    fields = "__all__" 
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Inventario añadido correctamente.'
 
    # Redirigimos a la página principal tras insertar el registro
    def get_success_url(self):        
        return reverse('Inventario')
 
#Para modificar un registro existente de la tabla Inventario_ventas
class InventarioActualizar(SuccessMessageMixin, UpdateView): 
    model = inventario_ventas
    form = inventario_ventas
    fields = "__all__"
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Inventario actualizado correctamente.'
 
    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('Inventario')
   


def buscar(request):

    if request.GET["registro"]:

        Codigo= request.GET["registro"]

        if len(Codigo)>5:

            mensaje="Código de ingreso no existe"
        
        else:

            Inventarios= inventario_ventas.objects.filter(id__icontains= Codigo)

            return render(request, "Inventario/detalles.html", {"Inventarios": Inventarios})
        
    else:

        mensaje="No has introducido nada"

    return HttpResponse(mensaje)