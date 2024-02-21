
from django.contrib import admin

# Register your models here.
from.models import arqueo 

#------------Administrador de status procesado de los atqueos de caja---------------------------------------

class ArqueoAdmin(admin.ModelAdmin):
    
    readonly_fields=('created','update')
    
admin.site.register(arqueo, ArqueoAdmin)

