# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import ControlesFronterizos, Usuario

class UsuarioCreationForm(forms.ModelForm):
    """
    Formulario para agregar usuarios en el admin, agrega una función
    clean-username que no consulta el modelo User,otra para verificar la 
    clave y otra para guardar la info.
    """  
    clave1 = forms.CharField(label="Clave", widget=forms.PasswordInput)
    clave2 = forms.CharField(label="Repite la clave", widget=forms.PasswordInput)
    
    class Meta():
        model = get_user_model()
        
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['Username_duplicado'])
        
    def clean_clave2(self):
        # Comprueba que coincidan ambas claves
        clave1 = self.cleaned_data.get("clave1")
        clave2 = self.cleaned_data.get("clave2")
        if clave1 and clave2 and clave1 != clave2:
            msg = "Las claves no coinciden"
            raise forms.ValidationError("Claves no coinciden")
        return clave2

    def save(self, commit=True):
        user = super(UsuarioCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["clave1"])
        if commit:
            user.save()
        return user
    
    
class UsuarioChangeForm(forms.ModelForm):
    """
    Formulario para cambiar datos del usuario
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()

    def clean_password(self):
        # siempre entrega el valor inicial
        return self.initial['password']
    
    
class UsuarioAdmin(admin.ModelAdmin):
    """
    Utiliza todas las configuraciones estandar de UserAdmin y cambia el form
    por defecto para agregar usuario con el form modificado 
    """
    add_form = UsuarioCreationForm
    # form = UsuarioChangeForm
    fields = ("username", "first_name", "last_name", "cargo", "region")
    list_display = ("username", "cargo", "region")
    
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ControlesFronterizos)
