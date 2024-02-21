
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from ArqueoCaja.views import NuevoArqueo, DetalleArqueo, ListaArqueo, ActualizarArqueo

urlpatterns = [

    #Formulario para nuevo registro de cierre
    path('ArqueoCaja/nuevo', NuevoArqueo.as_view(template_name = "Arqueo/nuevo.html"), name='Cierres'),

    #Página para realizar busqueda de un registro
    path('ArqueoCaja/buscar', ListaArqueo.as_view(template_name = "Arqueo/buscar.html"), name='Buscar'),

    #Página que muestra detalles del cierre
    path('ArqueoCaja/resultado/<int:pk>', DetalleArqueo.as_view(template_name = "Arqueo/buscar.html"), name='Resultados'),

    #Página que muestra detalles del cierre
    path('ArqueoCaja/detalle/<int:pk>', DetalleArqueo.as_view(template_name = "Arqueo/detalles.html"), name='Detalles'),

    #Formulario para editar registro
    path('ArqueoCaja/editar/<int:pk>', ActualizarArqueo.as_view(template_name = "Arqueo/actualizar.html"), name='Editar'),

    #Realizar busqueda por fecha de cierre
    path('ArqueoCaja/buscar_fecha/', views.buscar_fecha),

    #Realizar busqueda por código de caja
    path('ArqueoCaja/buscar_caja/', views.buscar_caja),

]
