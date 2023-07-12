from django.shortcuts import render, HttpResponse

from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    formulario_contacto= FormularioContacto
    return render(request, "contacto.html", {"miFormulario": formulario_contacto})


