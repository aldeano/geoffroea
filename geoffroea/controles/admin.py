# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, UserCreationForm, UserChangeForm
from .models import ControlesFronterizos, Usuario

class UsuarioCreationForm(UserCreationForm):
    """
    Formulario para agregar usuarios en el admin, agrega una función
    clean-username que no consulta el modelo User,otra para verificar la 
    clave y otra para guardar la info.
    """       
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
         
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['Username_duplicado'])

    
class UsuarioChangeForm(UserChangeForm):
    """
    Formulario para cambiar datos del usuario
    """
    class Meta(UserChangeForm.Meta):
        model = get_user_model()

    
class UsuarioAdmin(UserAdmin):
    """
    Utiliza todas las configuraciones estandar de UserAdmin y cambia el form
    por defecto para agregar usuario con el form modificado 
    """
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    #~ fieldsets = UserAdmin.fieldsets + (
        #~ (None, {'fields': ('cargo', 'region',)}),
    #~ )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'region', 'cargo', 'slug')}),
        (('Información Personal'), {'fields': ('first_name', 'last_name')}),
        (('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Fechas Importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1',
                       'password2', 'region', 'cargo')}
         ),
    )
    list_display = ("username", "cargo", "region", "slug", "get_full_name",)
    
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ControlesFronterizos)
