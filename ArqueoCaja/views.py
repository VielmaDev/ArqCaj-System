
#Importación de librería de vistas
from django.views.generic import ListView, DetailView 

#Importación de librería de edición
from django.views.generic.edit import CreateView, UpdateView

#Importación de librería de mensajería
from django.contrib.messages.views import SuccessMessageMixin 

#Importación de librería retorno
from django.urls import reverse
from django.shortcuts import render

#Importar zona horaria
from datetime import date

# Importando de tablas de la BD
from.models import arqueo 

# Create your views here.

# ------------------Cierre contable----------------------------

#Listar registros de cierres procesados de la tienda asignada
class ListaArqueo(ListView):

    def get(self, request, *args, **kwargs):
        query= arqueo.objects.filter(tienda=1)
        return render(request, "Arqueo/buscar.html", {"query": query})

#Detalles del registro del cierre
class DetalleArqueo(DetailView): 
    model =arqueo

#Nuevo registro de cierre  
class NuevoArqueo(SuccessMessageMixin, CreateView): 
    model =arqueo
    form =arqueo
    fields = "__all__" 
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Arqueo de caja registrado correctamente.'
 
    # Redirigimos a la página principal tras agregar el registro
    def get_success_url(self):        
        return reverse('Cierres')
    
#Modificar datos del cierre 
class ActualizarArqueo(SuccessMessageMixin, UpdateView): 
    model =arqueo
    form = arqueo
    fields = "__all__"
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Arqueo de caja actualizado correctamente.'
 
    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('Buscar')
    

#------------------Busqueda--------------------------

#Busqueda por fecha       
def buscar_fecha(request):

    #if request.GET["registro"]:

        Fecha= request.GET["registro"]

        if Fecha==None:
            mensaje="Debe ingresar una fecha"
            return render(request, "Arqueo/buscar.html")
        
        else:
            query= arqueo.objects.filter(created__icontains= Fecha).filter(tienda=1)
            return render(request, "Arqueo/index.html", {"query": query})
    #else:
        #mensaje="No se encontraron registros asociados"
    #return render(request, "Arqueo/buscar.html")


#Busqueda por código de caja     
def buscar_caja(request):

    #if request.GET["registro"]:

        Codigo= request.GET["registro"]

        if Codigo==None:
            mensaje="Código de caja no existe"
            return render(request, "Arqueo/buscar.html")
        else:
            query= arqueo.objects.filter(id__icontains= Codigo)
            return render(request, "Arqueo/index.html", {"query": query})
    #else:
        #mensaje="No se encontraron registros asociados"
    #return render(request, "Arqueo/buscar.html")








