
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Reportes.views import ListaCierre, DetalleCierre, ListaTiendas, DetalleTiendas, reporteExcelCierres, reporteExcelTiendas
from .import views


urlpatterns = [

    #Mostrar formulario de registros de cierres en general
    path('Reportes/', ListaCierre.as_view(template_name = "Reportes/reporteC.html"), name='ReporteC'),

    #Mostrar página con los detalles de los cierres en general
    path('Reportes/detalle/<int:pk>', DetalleCierre.as_view(template_name = "Reportes/reporteC.html"), name='BuscarC'),

    #Busqueda por fecha de cierres en general
    path('Reportes/buscar_fecha/', views.buscar_fecha),

    #genera un doc en formato Excel.
    path('Reportes/cierres/', reporteExcelCierres.as_view(), name='DocExcelCierres'),

    
    #Mostrar formulario de reporte de cierre por tienda
    path('Reportes/tiendas', ListaTiendas.as_view(template_name = "Reportes/reporteT.html"), name='ReporteT'),

    #Mostrar página con los detalle de cierre de tienda
    path('Reportes/detalle/<int:pk>', DetalleTiendas.as_view(template_name = "Reportes/reporteT.html"), name='BuscarT'),

    #Busqueda por cierre de tienda
    path('Reportes/buscar_tienda/', views.buscar_tienda),

    #genera un doc en formato Excel.
    path('Reportes/tiendas/', reporteExcelTiendas.as_view(), name='DocExcelTiendas'),


]
