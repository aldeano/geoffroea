from django.contrib import admin
from controles.models import *

class TipoUsuarioAdmin(admin.ModelAdmin):

    list_display = ("usuario", "tipo", "region")


admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(ControlesFronterizos)
