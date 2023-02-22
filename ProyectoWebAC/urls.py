
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ProyectoWebAC import views

from .views import logear, cerrar_sesion

urlpatterns = [

    path('home', views.home, name="Home"),
    path('tasa', views.tasa, name="Tasa"),
    path('',logear, name="Logear"),
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_sesion"),

    #path('', views.login, name="Login"),
    #path('cierre', views.cierre, name="Cierre"), se creo app
    #path('inventario', views.inventario, name="Inventario"), se creo app
    #path('reporte', views.reporte, name="Reporte"), se creo app
]
