
from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView
from .models import inventario_ventas
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

# Create your views here.

#Para obtener todos los registros de la tabla Inventario_ventas 
class InventarioListar(ListView): 
    model = inventario_ventas
 
#Para obtener todos los campos de un registro de la tabla Inventario_ventas 
class InventarioDetalle(DetailView): 
    model = inventario_ventas
 
#Para insertar un nuevo contacto en la tabla Inventario_ventas 
class InventarioNuevo(SuccessMessageMixin, CreateView): 
    model = inventario_ventas
    form = inventario_ventas
    fields = "__all__" 
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Inventario añadido correctamente.'
 
    # Redirigimos a la página principal tras insertar el registro
    def get_success_url(self):        
        return reverse('listar')
 
#Para modificar un contacto existente de la tabla Inventario_ventas
class InventarioActualizar(SuccessMessageMixin, UpdateView): 
    model = inventario_ventas
    form = inventario_ventas
    fields = "__all__"
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Inventario actualizado correctamente.'
 
    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('Inventario')
   

 