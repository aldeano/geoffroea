# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import View, CreateView, UpdateView, ListView, DetailView, DeleteView
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
        dicc = {"nombre": perfil.first_name, "region": perfil.get_region_display(), "cargo": perfil.get_cargo_display()}
        if perfil.cargo == "adm":
            template = "controles/admin.html"
        elif perfil.cargo == "er":
            template = "controles/er.html"
        elif perfil.cargo == "jf" or perfil.cargo == "insp":
            template = "controles/dia.html"
        
        return render(request, template, dicc)


class UsuarioMixin(object):
	
	def obtener_info_usuario(self):
		
		usuario = Usuario.objects.get(username=self.request.user.username)
		nombre = usuario.first_name
		region = usuario.get_region_display()
		cargo = usuario.get_cargo_display()
		
		return nombre, region, cargo 
		
	def get_context_data(self, **kwargs):
		
		contexto = super(UsuarioMixin, self).get_context_data(**kwargs)
		contexto['nombre'] = self.obtener_info_usuario()[0]
		contexto['region'] = self.obtener_info_usuario()[1]
		contexto['cargo'] = self.obtener_info_usuario()[2]
		
		return contexto


class ListarCCFF(UsuarioMixin, ListView):
    
    def get_queryset(self):
		self.usuario = get_object_or_404(Usuario, username=self.request.user.username)
		return ControlesFronterizos.objects.filter(region=self.usuario.region)


class AgregarCCFF(UsuarioMixin, CreateView):
    
    model = ControlesFronterizos
    form_class = FormularioCCFF
    success_url = reverse_lazy('listar_ccff')
    
    def get_form_kwargs(self):
        kwargs = super(AgregarCCFF, self).get_form_kwargs()
        kwargs.update({'usuario': self.request.user})
        return kwargs
    

class BorrarCCFF(UsuarioMixin, DeleteView):
	
	model = ControlesFronterizos
	success_url = reverse_lazy('listar_ccff')


class ModificarCCFF(UsuarioMixin, UpdateView): 

	model = ControlesFronterizos
	form = FormularioCCFF
	success_url = reverse_lazy('listar_ccff')


class ListarInspector(UsuarioMixin, ListView):
    
    def get_queryset(self):
		self.usuario = get_object_or_404(Usuario, username=self.request.user.username)
		return Usuario.objects.filter(region__exact=self.usuario.region)

	    
class AgregarInspector(UsuarioMixin, CreateView):
    
    model = Usuario
    form_class = FormularioPerfil
    success_url = reverse_lazy('listar_insp')


class BorrarInspector(UsuarioMixin, DeleteView):
	
	model = Usuario
	

class ModificarInspector(UsuarioMixin, UpdateView):

	model = Usuario
	form_class = FormularioPerfil
	
	def get_object(self, queryset=None):
		obj = Usuario.objects.get(id=self.kwargs['id'])
		return obj

class Salir(View):
    
    def get(self,request):
        
        logout(request)
        return redirect('inicio')


