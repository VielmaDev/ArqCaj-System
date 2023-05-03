from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

from .models import tienda, divisas

# Create your views here.

#Para obtener todos los campos de un registro de la tabla Inventario_ventas 

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

class HomeDetalle(DetailView): 
    model = tienda

def home(request):
    Tienda= tienda.objects.all()
    Divisa= divisas.objects.all()
    return render(request, "ProyectoWebAC/home.html", {"Tiendas": Tienda, "Divisas": Divisa})



