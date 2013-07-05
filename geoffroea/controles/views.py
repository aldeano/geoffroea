# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Usuario
from .forms import FormularioPerfil, FormularioDia, FormularioCCFF

class PortadaFuri(View):

    def get(self, request):
        
        formulario = AuthenticationForm()
        dicc = {'formulario': formulario}
        return render(request, "index.html", dicc)

    def post(self, request, *args, **kwargs):
        
        formulario = AuthenticationForm(data=request.POST)
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
        else:
            return render(request, 'index.html', dicc)
    
    
class GestionRegistros(View):

    def get(self, request):
        
        digitador = request.user.username
        perfil = Usuario.objects.get(username=digitador)
        dicc = {"nombre": perfil.first_name, "region": perfil.region, "cargo": perfil.cargo}
        if perfil.cargo == "adm":
            template = "gestion/admin.html"
        elif perfil.cargo == "er":
            formulario_perfil = FormularioPerfil()
            formulario_ccff = FormularioCCFF()
            dicc["form_perfil"] = formulario_perfil
            dicc["form_ccff"] = formulario_ccff
            template = "gestion/er.html"
        elif perfil.cargo == "jf" or perfil.cargo == "insp":
            formulario_dia = FormularioDia()
            dicc["form_dia"] = formulario_dia
            template = "gestion/dia.html"
        
        return render(request, template, dicc)


class Salir(View):
    
    def get(self,request):
        
        logout(request)
        return redirect('inicio')
