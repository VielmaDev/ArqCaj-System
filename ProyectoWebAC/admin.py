
from django.contrib import admin
from.models import tienda, usuario, divisas

# Register your models here.

class TiendaAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')

admin.site.register(tienda, TiendaAdmin)


class UsuarioAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')

admin.site.register(usuario, UsuarioAdmin)

class DivisaAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'update')

admin.site.register(divisas, DivisaAdmin)



