
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ProyectoWebAC import views
from .views import logear, cerrar_sesion
from ProyectoWebAC.views import HomeDetalle
from .import views

urlpatterns = [

    path('',logear, name="Logear"),
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_sesion"),
    
    path('home', views.home, name="Home"),

    #Mostrar una página con el detalle de la(s) tienda(s)
    #path('ProyectoWebAC/home/<int:pk>', HomeDetalle.as_view(template_name = "ProyectoWebAC/home.html"), name="Home"),


]
