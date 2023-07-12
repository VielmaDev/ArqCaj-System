
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
from .models import arqueo
from ProyectoWebAC.models import caja, tasa
from Ingresos.models import ventas

# Create your views here.
# ------------------Ingresos de ventas----------------------------

#Para obtener todos los registros de la tabla arqueo
class ListaArqueo(ListView): 
    model =arqueo
 
#Para obtener todos los campos de un registro de la tabla arqueo
class DetalleArqueo(DetailView): 
    model = arqueo

#Para registrar los ingresos 
class NuevoArqueo(SuccessMessageMixin, CreateView): 
    model = arqueo
    form = arqueo
    fields = "__all__" 
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Ingreso de venta registrado correctamente.'
 
    # Redirigimos a la página principal tras agregar el registro
    def get_success_url(self):        
        return reverse('Cierres')
    
#Para modificar datos en la tabla arqueo
class ActualizarArqueo(SuccessMessageMixin, UpdateView): 
    model =arqueo
    form = arqueo
    fields = "__all__"
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Ingreso de venta actualizado correctamente.'
 
    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('Cierres')
    
#----------------------------------------------------------

def buscar(request):

    if request.GET["registro"]:

        Codigo= request.GET["registro"]

        if len(Codigo)>5:

            mensaje="Código de ingreso no existe"
        
        else:

            Arqueos= arqueo.objects.filter(id__icontains= Codigo)

            return render(request, "Arqueo/detalles.html", {"Arqueos": Arqueos})
        
    else:

        mensaje="No has introducido nada"

    return HttpResponse(mensaje) 



class ListaCaja(ListView):
    model=caja
    
def cajas(request):
    Caja= caja.objects.all()
    return render(request, "ArqueoCaja/nuevo.html", {"Cajas": Caja})

def divisa(request):
    Divisa= tasa.objects.all()
    return render(request, "ArqueoCaja/nuevo.html", {"Divisas": Divisa})

def venta(request):
    Ingreso= ventas.objects.all()
    return render(request, "Ingresos/nuevo.html", {"Ingresos": Ingreso })


