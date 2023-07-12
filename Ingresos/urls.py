
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Ingresos.views import ListaIngresos, DetalleIngresos, NuevoIngresos, ActualizarIngresos

from .import views

urlpatterns = [

    #Mostrar formulario de alta de nuevo registro
    path('Ingresos/', ListaIngresos.as_view(template_name = "Ingresos/index.html"), name='Caja'),

    #Mostrar una página con el detalle del registro
    path('Ingresos/detalle/<int:pk>', DetalleIngresos.as_view(template_name = "Ingresos/detalles.html"), name='Detalles'),
 
    #Mostrar todos los registros en una tabla
    path('Ingresos/nuevo', NuevoIngresos.as_view(template_name = "Ingresos/nuevo.html"), name='Nuevos'),

    #Mostrar formulario de modificación de registro
    path('Ingresos/editar/<int:pk>', ActualizarIngresos.as_view(template_name = "Ingresos/actualizar.html"), name='Actualizar'), 

    path('Ingresos/buscar/', views.buscar)


]
