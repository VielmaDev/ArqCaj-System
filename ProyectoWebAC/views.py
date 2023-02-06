from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import tienda, usuario, divisas

# Create your views here.

def login(request):
    #return HttpResponse("Autenticacion")
    return render(request, "login/login.html")

def home(request):
    #return HttpResponse("Home")
    Tienda= tienda.objects.all()
    Usuario= usuario.objects.all()
    Divisa= divisas.objects.all()
    return render(request, "ProyectoWebAC/home.html", {"Tiendas": Tienda, "Usuarios": Usuario, "Divisas": Divisa})
    

def cierre(request):
    #return HttpResponse("cierre")
    return render(request, "ProyectoWebAC/cierre.html")

def inventario(request):
    #return HttpResponse("Inventario")
    return render(request, "ProyectoWebAC/inventario.html")

def tasa(request):
    #return HttpResponse("Tasa_cambio")
    return render(request, "ProyectoWebAC/tasa.html")

def reporte(request):
    #return HttpResponse("Reporte")
    return render(request, "ProyectoWebAC/reporte.html")

def cerrar_sesion(request):

    logout(request)
    return redirect(login)

-------------------------------------------------------------

def logear(request):

    if request.method=="POST":

        form= AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("usuario")
            contra=form.cleaned_data.get("contrasena")
            usuario=authenticate(usuario=nombre_usuario, contrasena=contra)

            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Información incorrecta")
        else:
            
            messages.error(request, "usuario no valido")

    form=AuthenticationForm()

    return render(request,"login/login.html", {"form": form})