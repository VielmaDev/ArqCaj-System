from django.shortcuts import render

# Create your views here.

def reporte(request):
    #return HttpResponse("Reporte")
    return render(request, "Reportes/reporte.html")