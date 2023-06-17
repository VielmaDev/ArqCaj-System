
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ArqueoCaja.views import ListaIngresos, NuevoIngresos, ActualizarIngresos, DetalleIngresos
from ArqueoCaja.views import NuevoArqueo

from .import views

urlpatterns = [
    
    #path('cierre', views.cierre, name="Cierre"),

    #Mostrar formulario de alta de nuevo registro
    path('ArqueoCaja/', ListaIngresos.as_view(template_name = "Ingresos/index.html"), name='Caja'),
 
    #Mostrar todos los registros en una tabla
    path('ArqueoCaja/nuevo', NuevoIngresos.as_view(template_name = "Ingresos/ingresos.html"), name='Ingresos'),

    #Mostrar formulario de modificación de registro
    path('ArqueoCaja/editar/<int:pk>', ActualizarIngresos.as_view(template_name = "Ingresos/actualizar.html"), name='Actualizar'), 

    #Mostrar una página con el detalle del registro
    path('ArqueoCaja/detalle/<int:pk>', DetalleIngresos.as_view(template_name = "Ingresos/arqueo.html"), name='Arqueo'),

    #Mostrar todos los registros en una tabla
    #path('ArqueoCaja/arqueo', NuevoArqueo.as_view(template_name = "Ingresos/arqueo.html"), name='Arqueo'),

]
