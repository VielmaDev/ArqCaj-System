
#Importación de librería de vistas
from django.views.generic import ListView, DetailView 

#Importación de librería de edición
from django.views.generic.edit import CreateView, UpdateView

#Importación de librería de mensajería
from django.contrib.messages.views import SuccessMessageMixin 

#Importación de librería retorno
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse

#Formularios
from django import forms

#Importación de las BD
from .models import ventas
#from ProyectoWebAC.models import caja, tasa

# Create your views here.
# ------------------Ingresos de ventas----------------------------

#Para obtener todos los registros de la tabla arqueo
class ListaIngresos(ListView): 
    model =ventas
 
#Para obtener todos los campos de un registro de la tabla arqueo
class DetalleIngresos(DetailView): 
    model = ventas

#Para registrar los ingresos 
class NuevoIngresos(SuccessMessageMixin, CreateView): 
    model = ventas
    form = ventas
    fields = "__all__" 
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Ingreso de venta registrado correctamente.'
 
    # Redirigimos a la página principal tras agregar el registro
    def get_success_url(self):        
        return reverse('Caja')
    
#Para modificar datos en la tabla arqueo
class ActualizarIngresos(SuccessMessageMixin, UpdateView): 
    model =ventas
    form = ventas
    fields = "__all__"
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Ingreso de venta actualizado correctamente.'
 
    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('Caja')
    

# Realizar busqueda por parametros        
def buscar_codigo(request):

    if request.GET["registro"]:
        Codigo= request.GET["registro"]

        if Codigo==None:
            mensaje="Código no esta asociado a ningun registro"
        
        else:
            Ventas= ventas.objects.filter(id__icontains= Codigo)
            return render(request, "Ingresos/resultado.html", {"Ventas": Ventas})
        
    else:
        mensaje="No se encontraron registros asociados"
    return render(request, "Ingresos/resultado.html")

      
def buscar_fecha(request):

    if request.GET["registro"]:
        Fecha= request.GET["registro"]

        if Fecha==None:
            mensaje="Fecha no esta asociado a ningun registro"
        
        else:
            Ventas= ventas.objects.filter(created__icontains= Fecha)
            return render(request, "Ingresos/resultado.html", {"Ventas": Ventas})
        
    else:
        mensaje="No se encontraron registros asociados"
    return render(request, "Ingresos/resultado.html")




   
    

    


                        


    
  