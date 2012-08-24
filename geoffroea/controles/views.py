# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def ingresar(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		dicc = {'formulario': formulario}
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate[username:usuario, password:clave]
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/ingreso')
				else:
					return render(request, 'index.html', dicc)
			else:
				return render(request, 'index.html', dicc)
	else:
		formulario = AuthenticationForm()
		dicc = {'formulario': formulario}
		return render(request, 'index.html', dicc)