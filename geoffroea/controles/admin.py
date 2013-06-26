# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, UserCreationForm
from .models import ControlesFronterizos, Usuario

class UsuarioCreationForm(UserCreationForm):
    """
    Formulario para agregar usuarios en el admin, agrega una función
    clean-username que no consulta el modelo User
    """
    
    class Meta(UserCreationForm.Meta):
        model = Usuario

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['Username_duplicado'])
    

class UsuarioAdmin(admin.ModelAdmin):
    """
    Utiliza todas las configuraciones estandar de UserAdmin y cambia el form
    por defecto para agregar usuario con el form modificado 
    """
    add_form = UsuarioCreationForm    
    
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ControlesFronterizos)
