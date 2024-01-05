from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import View

#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin 
#from django import forms

#Consulta de registro
from django.views.generic import ListView, DetailView 


#Importación de tabla tienda y tasa
from .models import tienda,tasaDolar, tasaEuro, comunicado

# Importando tabla arqueo de la app ArqueoCaja
from ArqueoCaja.models import arqueo 

# Importando tabla inventario_ventas de la app Inventario
from Inventario.models import inventario_ventas 

# Create your views here.


#Función iniciar sesión
def logear(request):

    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            nombre=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username= nombre, password=contra)

            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no validado")
        else:
            messages.error(request, "Información no valida")

    form=AuthenticationForm()
    return render (request, "login/login.html",{"form": form})

#Función cerrar sesión
def cerrar_sesion(request):
    logout (request)
    return redirect('Logear')

def baseII(request):
    Tienda= tienda.objects.all()
    dolar= tasaDolar.objects.all()
    euro= tasaEuro.objects.all()
    return render(request, "ProyectoWebAC/baseII.html", {"Tiendas": Tienda, "dolars": dolar, "euros": euro,})

def home(request):
    Dolar= tasaDolar.objects.all()
    Euro= tasaEuro.objects.all()
    Arqueo= arqueo.objects.all()
    Nota= comunicado.objects.all()
    return render(request, "ProyectoWebAC/home.html", {"Dolars": Dolar,"Euros": Euro,"Arqueos": Arqueo, "Notas": Nota,})



