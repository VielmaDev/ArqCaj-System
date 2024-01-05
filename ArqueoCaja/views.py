
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
from ProyectoWebAC.models import caja, tasaDolar, tasaEuro

# Create your views here.

# ------------------Cierre contable----------------------------

#Lista (indice) de los registros del cierre
class ListaArqueo(ListView): 
    model =arqueo

#Buscar registros del cierre
class BuscarArqueo(ListView): 
    model =arqueo
 
#Detalles del registro del cierre
class DetalleArqueo(DetailView): 
    model =arqueo

#Nuevo registro de cierre  
class NuevoArqueo(SuccessMessageMixin, CreateView): 
    model =arqueo
    form =arqueo
    fields = "__all__" 
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Ingreso de venta registrado correctamente.'
 
    # Redirigimos a la página principal tras agregar el registro
    def get_success_url(self):        
        return reverse('Cierres')
    
#Modificar datos del cierre 
class ActualizarArqueo(SuccessMessageMixin, UpdateView): 
    model =arqueo
    form = arqueo
    fields = "__all__"
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Ingreso de venta actualizado correctamente.'
 
    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('Cierres')
    

#------------------Busqueda--------------------------

#Busqueda por fecha       
def buscar_fecha(request):

    if request.GET["registro"]:

        Fecha= request.GET["registro"]

        if Fecha==None:
            mensaje="Fecha no esta asociado a ningun registro"
        
        else:
            Arqueos= arqueo.objects.filter(created__icontains= Fecha)
            return render(request, "Arqueo/index.html", {"Arqueos": Arqueos})
    else:
        mensaje="No se encontraron registros asociados"
    return render(request, "Arqueo/buscar.html")

#Busqueda por código      
def buscar_codigo(request):

    if request.GET["registro"]:

        Codigo= request.GET["registro"]

        if Codigo==None:
            mensaje="Código no esta asociado a ningun registro"
        else:
            Arqueos= arqueo.objects.filter(id__icontains= Codigo)
            return render(request, "Arqueo/index.html", {"Arqueos": Arqueos})
    else:
        mensaje="No se encontraron registros asociados"
    return render(request, "Arqueo/buscar.html")


#------Datos precargados en sistema--------

def nuevo(request):
    Caja= caja.objects.all()
    Dolar=tasaDolar.objects.all()
    Euro=tasaEuro.objects.all()
    
    return render(request, "ArqueoCaja/nuevo.html", {"Cajas":Caja,"Dolas":Dolar,"Euro":Euro,})





