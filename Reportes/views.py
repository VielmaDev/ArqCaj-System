
from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView
from Inventario.models import inventario_ventas
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

# Create your views here.

#def reporte(request):
    #return HttpResponse("Reporte")
    return render(request, "Reportes/reporte.html")

