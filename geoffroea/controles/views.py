# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import TipoUsuario
from .forms import FormularioPerfil

class PortadaFuri(View):

    def get(self, request):
        
        formulario = AuthenticationForm()
        dicc = {'formulario': formulario}
        return render(request, "index.html", dicc)

    def post(self, request, *args, **kwargs):
        
        formulario = AuthenticationForm(request.POST)
        dicc = {'formulario': formulario}
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return redirect('gestion_registros')
                else:
                    return render(request, 'index.html', dicc)
            else:
                return render(request, 'index.html', dicc)

class GestionRegistros(View):

    def get(self, request):
        
        digitador = request.user
        perfil = TipoUsuario.objects.get(usuario=digitador)
        formulario_usuario = UserCreationForm()
        formulario_perfil = FormularioPerfil()
        dicc = {"nombre": perfil.nombre, "region": perfil.region, "form_usuario": formulario_usuario, "form_perfil": formulario_perfil}
        return render(request, "ingreso.html", dicc)


class Salir(View):
    
    def get(self,request):
        
        logout(request)
        return redirect('inicio')
