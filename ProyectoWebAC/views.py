from django.shortcuts import render,HttpResponse

# Create your views here.

def login(request):
    #return HttpResponse("Autenticacion")
    return render(request, "ProyectoWebAC/login.html")

def home(request):
    #return HttpResponse("Home")
    return render(request, "ProyectoWebAC/home.html")

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
