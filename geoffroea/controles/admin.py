# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ControlesFronterizos, Usuario

# class TipoUsuarioAdmin(admin.ModelAdmin):

    # list_display = ("usuario", "tipo", "region")

# admin.site.register(TipoUsuario, TipoUsuarioAdmin)
    

admin.site.register(Usuario, UserAdmin)
admin.site.register(ControlesFronterizos)
