

#Importación de librería de vistas
from django.views.generic import ListView, DetailView 

#Importación de librería de edición
from django.views.generic.edit import CreateView, UpdateView

#Importación de librería de mensajería
from django.contrib.messages.views import SuccessMessageMixin 

#Importación de librería retorno
from django.urls import reverse
from django.shortcuts import render

#Formularios
from django import forms

#Importación de las BD
from .models import ingresos, arqueo
from ProyectoWebAC.models import caja, tasa

# Create your views here.
# ------------------Ingresos de ventas----------------------------

#Para obtener todos los registros de la tabla arqueo
class ListaIngresos(ListView): 
    model =ingresos
 
#Para obtener todos los campos de un registro de la tabla arqueo
class DetalleIngresos(DetailView): 
    model = ingresos

#Para registrar los ingresos 
class NuevoIngresos(SuccessMessageMixin, CreateView): 
    model = ingresos
    form = ingresos
    fields = "__all__" 
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Ingreso de venta registrado correctamente.'
 
    # Redirigimos a la página principal tras agregar el registro
    def get_success_url(self):        
        return reverse('Caja')
    
#Para modificar datos en la tabla arqueo
class ActualizarIngresos(SuccessMessageMixin, UpdateView): 
    model =ingresos
    form = ingresos
    fields = "__all__"
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Ingreso de venta actualizado correctamente.'
 
    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('Caja')
    

#-----------------Cierre contable------------------------
    
#Para procesar el arqueo de caja
class NuevoArqueo(SuccessMessageMixin, CreateView): 
    model = arqueo
    form = arqueo
    fields = "__all__" 
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Arqueo de caja registrado correctamente.'
 
    # Redirigimos a la página principal tras agregar el registro
    def get_success_url(self):        
        return reverse('Caja')

#----------------------------------------------------------
    
def caja(request):
    Caja= caja.objects.all()
    return render(request, "ArqueoCaja/nuevo.html", {"Cajas": Caja})

def divisa(request):
    Divisa= tasa.objects.all()
    return render(request, "ArqueoCaja/nuevo.html", {"Divisas": Divisa})


 
 #def cierre(request):
    #return HttpResponse("cierre")
    #return render(request, "ProyectoWebAC/cierre.html")
   # return render(request, "ArqueoCaja/cierre.html")
   