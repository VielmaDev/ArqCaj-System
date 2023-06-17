
from django.contrib import admin
from.models import tienda, tasa,caja

# Register your models here.

class TiendaAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')

admin.site.register(tienda, TiendaAdmin)


class DivisaAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')

admin.site.register(tasa, DivisaAdmin)


class CajaAdmin(admin.ModelAdmin):
    
    readonly_fields=('created', 'update')

admin.site.register(caja, CajaAdmin)



