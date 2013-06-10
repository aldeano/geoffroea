# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

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
        
        dicc = {"resultado": "vas bien parece"}
        return render(request, "ingreso.html", dicc)
