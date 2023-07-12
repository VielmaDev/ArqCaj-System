
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ArqueoCaja.views import ListaArqueo, NuevoArqueo, ActualizarArqueo, DetalleArqueo

from .import views

urlpatterns = [

    #Mostrar formulario de alta de nuevo registro
    path('ArqueoCaja/', ListaArqueo.as_view(template_name = "Arqueo/index.html"), name='Cierres'),

    #Mostrar una página con el detalle del registro
    path('ArqueoCaja/detalle/<int:pk>', DetalleArqueo.as_view(template_name = "Arqueo/detalles.html"), name='Detalles'),
 
    #Mostrar todos los registros en una tabla
    path('ArqueoCaja/nuevo', NuevoArqueo.as_view(template_name = "Arqueo/nuevo.html"), name='Nuevos'),

    #Mostrar formulario de modificación de registro
    path('ArqueoCaja/editar/<int:pk>', ActualizarArqueo.as_view(template_name = "Arqueo/actualizar.html"), name='Actualizar'), 

    path('ArqueoCaja/buscar/', views.buscar)

]
