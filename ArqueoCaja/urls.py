
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ArqueoCaja.views import ListaArqueo, NuevoArqueo, DetalleArqueo, BuscarArqueo, ActualizarArqueo 

from .import views

urlpatterns = [

    #Formulario para nuevo registro de cierre
    path('ArqueoCaja/nuevo', NuevoArqueo.as_view(template_name = "Arqueo/nuevo.html"), name='Cierres'),

    #Página para realizar busqueda de un registro
    path('ArqueoCaja/buscar', BuscarArqueo.as_view(template_name = "Arqueo/buscar.html"), name='Buscar'),

    #Página que muestra detalles del cierre
    path('ArqueoCaja/resultado/<int:pk>', DetalleArqueo.as_view(template_name = "Arqueo/resultado.html"), name='Resultados'),

    #Página que muestra detalles del cierre
    path('ArqueoCaja/detalle/<int:pk>', DetalleArqueo.as_view(template_name = "Arqueo/detalles.html"), name='Detalles'),

    #Formulario para editar registro
    path('ArqueoCaja/editar/<int:pk>', ActualizarArqueo.as_view(template_name = "Arqueo/actualizar.html"), name='Actualizar'), 

    #Realizar busqueda por fecha de cierre
    path('ArqueoCaja/buscar_fecha/', views.buscar_fecha),
    
    #Realizar busqueda por código de cierre
    path('ArqueoCaja/buscar_codigo/', views.buscar_codigo),

]
