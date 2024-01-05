
from django.contrib import admin
from.models import tienda, caja, tasaDolar,tasaEuro, comunicado

# Register your models here.

#------------------Tienda------------------

class TiendaAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')

admin.site.register(tienda, TiendaAdmin)

#------------------Caja------------------

class CajaAdmin(admin.ModelAdmin):
    
    readonly_fields=('created', 'update')

admin.site.register(caja, CajaAdmin)

#-----------------Tasa Dolar----------------

class DolarAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')

admin.site.register(tasaDolar, DolarAdmin)

#------------------Tasa Euro------------------

class EuroAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')

admin.site.register(tasaEuro, EuroAdmin)

#------------------Comunicado------------------

class ComunicadoAdmin(admin.ModelAdmin):
    
    readonly_fields=('created', 'update')

admin.site.register(comunicado, ComunicadoAdmin)



