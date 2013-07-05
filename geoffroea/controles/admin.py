# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import ControlesFronterizos, Usuario

class UsuarioCreationForm(UserCreationForm):
    """
    Formulario para agregar usuarios en el admin, agrega una función
    clean-username que no consulta el modelo User,otra para verificar la 
    clave y otra para guardar la info.
    """  
    # password1 = forms.CharField(label="Clave", widget=forms.PasswordInput)
    # password2 = forms.CharField(label="Repite la clave", widget=forms.PasswordInput)
    
      
    class Meta():
        model = get_user_model()
        # fields = ("username", "cargo", "region")
         
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['Username_duplicado'])
        
    # def clean_password2(self):
        # Comprueba que coincidan ambas claves
        # password1 = self.cleaned_data.get("password1")
        # password2 = self.cleaned_data.get("password2")
        # if password1 and password2 and password1 != password2:
            # msg = "Las claves no coinciden"
            # raise forms.ValidationError("Claves no coinciden")
        # return password2

    # def save(self, commit=True):
        # user = super(UsuarioCreationForm, self).save(commit=False)
        # user.set_password(self.cleaned_data["password1"])
        # if commit:
            # user.save()
        # return user
    
    
class UsuarioChangeForm(UserChangeForm):
    """
    Formulario para cambiar datos del usuario
    """
    # password = ReadOnlyPasswordHashField()
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # fields = ("username", "cargo", "region")
            
    # def clean_password2(self):
        # Comprueba que coincidan ambas claves
        # password1 = self.cleaned_data.get("password1")
        # password2 = self.cleaned_data.get("password2")
        # if password1 and password2 and password1 != password2:
            # msg = "Las claves no coinciden"
            # raise forms.ValidationError("Claves no coinciden")
        # return password2
    
    # def clean_password(self):
        # siempre entrega el valor inicial
        # return self.initial['password']
    
    
class UsuarioAdmin(UserAdmin):
    """
    Utiliza todas las configuraciones estandar de UserAdmin y cambia el form
    por defecto para agregar usuario con el form modificado 
    """
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cargo', 'region',)}),
    )
    list_display = ("username", "cargo", "region")
    # fields = ("cargo", "region")
    
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(ControlesFronterizos)
