# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario, ControlesFronterizos
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
        
        usuario = request.user
        perfil = Usuario.objects.get(username=usuario.username)
        dicc = {"nombre": perfil.first_name, "region": perfil.region, "cargo": perfil.cargo}
        if perfil.cargo == "adm":
            template = "controles/admin.html"
        elif perfil.cargo == "er":
            template = "controles/er.html"
        elif perfil.cargo == "jf" or perfil.cargo == "insp":
            template = "controles/dia.html"
        
        return render(request, template, dicc)

class AgregarCCFF(CreateView):
    
    model = ControlesFronterizos
        
    def get_context_data(self, **kwargs):
        
        context = super(AgregarCCFF, self).get_context_data(**kwargs)
        usuario = Usuario.objects.get(username=self.request.user.username)
        context['form'] = FormularioCCFF(usuario)
        context['nombre'] = usuario.first_name
        context['region'] = usuario.get_region_display()
        context['cargo'] = usuario.get_cargo_display()
        
        return context
    
    
class ModificarCCFF(UpdateView): 
    
    model = ControlesFronterizos
    form = FormularioCCFF
    
    
class AgregarInspector(CreateView):
    
    pass


class ModificarInspector(UpdateView):
    
    pass


class Salir(View):
    
    def get(self,request):
        
        logout(request)
        return redirect('inicio')


