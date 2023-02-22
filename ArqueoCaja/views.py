from django.shortcuts import render

# Create your views here.
def cierre(request):
    #return HttpResponse("cierre")
    #return render(request, "ProyectoWebAC/cierre.html")
    return render(request, "ArqueoCaja/cierre.html")