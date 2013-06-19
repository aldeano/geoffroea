# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import TipoUsuario

class FormularioPerfil(ModelForm):
	
	class Meta:
		model = TipoUsuario