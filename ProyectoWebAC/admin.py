
from django.contrib import admin

# Register your models here.
from.models import tienda, caja, tasaDivisa,comunicado


#---------------Administrador de Tiendas------------------

class TiendaAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')

admin.site.register(tienda, TiendaAdmin)

#------------------Administrador de Caja------------------

class CajaAdmin(admin.ModelAdmin):
    
    readonly_fields=('created', 'update')

admin.site.register(caja, CajaAdmin)

#------------------Administrador Tasa Divisa----------------

class DivisaAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')

admin.site.register(tasaDivisa, DivisaAdmin)

#----------------Administrador de Comunicado------------------

class ComunicadoAdmin(admin.ModelAdmin):
    
    readonly_fields=('created', 'update')

admin.site.register(comunicado, ComunicadoAdmin)



