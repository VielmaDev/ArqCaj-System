from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import tienda, usuario, divisas

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
            messages.error(request, "Información incorrecta")

    form=AuthenticationForm()
    return render (request, "login/login.html",{"form": form})

#Función cerrar sesión
def cerrar_sesion(request):
    
    logout (request)
    return redirect('Logear')

def home(request):
    #return HttpResponse("Home")
    Tienda= tienda.objects.all()
    Usuario= usuario.objects.all()
    Divisa= divisas.objects.all()
    return render(request, "ProyectoWebAC/home.html", {"Tiendas": Tienda, "Usuarios": Usuario, "Divisas": Divisa})
    
def tasa(request):
    #return HttpResponse("Tasa_cambio")
    return render(request, "ProyectoWebAC/tasa.html")



#En construcción-----------------------------------------

#class Acceso(View):

    #def get(self, request):
        #form=UserCreationForm()
        #return render (request, "login/login.html", {"form": form})

    #def post(self, request):
        #pass


#-------------------------------------------

#def login(request):
    #return HttpResponse("Autenticacion")
    #return render(request, "login/login.html")