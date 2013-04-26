# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


# def IngresoFuri(request):
#   if request.method == 'POST':
#       formulario = AuthenticationForm(request.POST)
#       dicc = {'formulario': formulario}
#       if formulario.is_valid:
#           usuario = request.POST['username']
#           clave = request.POST['password']
#           acceso = authenticate[username:usuario, password:clave]
#           if acceso is not None:
#               if acceso.is_active:
#                   login(request, acceso)
#                   return redirect('gestion_registros')
#               else:
#                   return render(request, 'index.html', dicc)
#           else:
#               return render(request, 'index.html', dicc)
#   else:
#       formulario = AuthenticationForm()
#       dicc = {'formulario': formulario}
#       return render(request, 'index.html', dicc)

class PortadaFuri(TemplateView):

    template_name = "index.html"    


class GestionRegistros(View):

    template_name = "ingreso.html"

    def post(self, request, *args, **kwargs):
        '''
        Función que recibe el tipo de funcionario y le devuelve una página en la cual
        puede editar los registros a los que tiene permiso y puede hacer consultas
        de todos los datos disponibles
        '''
        tipo_usuario = request.user.get_profile().tipo
        dicc = {'tipo_usuario': tipo_usuario}

        return render(request, template_name, dicc)
