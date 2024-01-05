
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Ingresos.views import ListaIngresos

from .import views

urlpatterns = [

    path('Reportes/buscar_fecha/', views.buscar_fecha),

    #Mostrar formulario de alta de nuevo registro
    path('Reportes/', ListaIngresos.as_view(template_name = "Reportes/reporteA.html"), name='ReporteA'),

    #Mostrar una página con el detalle del registro
    #path('Ingresos/detalle/<int:pk>', DetalleIngresos.as_view(template_name = "Ingresos/detalles.html"), name='Detalles'),

]
