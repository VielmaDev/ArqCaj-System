
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Inventario.views import InventarioListar, InventarioDetalle, InventarioNuevo, InventarioActualizar
#from .import views

urlpatterns = [
    
    #path('inventario', views.inventario, name="Inventario"),

    #Mostrar todos los registros en una tabla
    path('Inventario/', InventarioListar.as_view(template_name = "Inventario/index.html"), name='Inventario'),
 
    #Mostrar formulario de alta de nuevo registro
    path('Inventario/detalle/<int:pk>', InventarioDetalle.as_view(template_name = "Inventario/detalles.html"), name='Detalles'),

    #Mostrar todos los registros en una tabla
    path('Inventario/nuevo', InventarioNuevo.as_view(template_name = "Inventario/nuevo.html"), name='Nuevo'),
 
    #Mostrar formulario de modificación de registro
    path('Inventario/editar/<int:pk>', InventarioActualizar.as_view(template_name = "Inventario/actualizar.html"), name='Actualizar'), 
    
]
