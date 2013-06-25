# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Usuario, ControlesFronterizos, Dia_CCFF_Terrestre

class FormularioPerfil(ModelForm):
	
	class Meta:
		model = Usuario
		exclude = ('usuario',)


class FormularioCCFF(ModelForm):
    
    class Meta:
        model = ControlesFronterizos
        

class FormularioDia(ModelForm):
    
    class Meta:
        model = Dia_CCFF_Terrestre
