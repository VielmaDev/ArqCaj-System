
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Inventario.views import InventarioListar, InventarioNuevo, InventarioActualizar
#from .import views

urlpatterns = [

    #path('reporte', views.reporte, name="Reporte")

    #Mostrar todos los registros en una tabla
    path('Reportes/', InventarioListar.as_view(template_name = "Reportes/inventario.html"), name='Inventario'),
 
    #Mostrar formulario de alta de nuevo registro
    path('Reportes/nuevo', InventarioNuevo.as_view(template_name = "Reportes/crear.html"), name='Nuevo'),
 
    #Mostrar formulario de modificación de registro
    path('Reportes/editar/<int:pk>', InventarioActualizar.as_view(template_name = "Reportes/actualizar.html"), name='Actualizar'), 
    
]
