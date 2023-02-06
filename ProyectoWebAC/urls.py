
from django.urls import path
from ProyectoWebAC import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.login, name="Login"),
    path('home', views.home, name="Home"),
    path('cierre', views.cierre, name="Cierre"),
    path('inventario', views.inventario, name="Inventario"),
    path('tasa', views.tasa, name="Tasa"),
    path('reporte', views.reporte, name="Reporte")
]
