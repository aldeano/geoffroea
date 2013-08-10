# -*- coding: utf-8 -*-
from django import forms
from .models import Usuario, ControlesFronterizos, Dia_CCFF_Terrestre

class FormularioPerfil(forms.ModelForm):
	# estas opciones están fijas porque el formulario sólo se ocupa en el
	# frontend por parte de los encargados regionales, quienes sólo pueden
	# asignar jefes o inspectores.
			
	def __init__(self, *args, **kwargs):
		opciones = (("jf", "Jefe(a) de Turno"),
				("insp", "Inspector(a)"))
		super(FormularioPerfil, self).__init__(*args, **kwargs)
		self.fields["cargo"] = forms.ChoiceField(choices=opciones)
	
	class Meta:
		model = Usuario
		fields = ("username", "password", "first_name", "last_name", "cargo",)


class FormularioCCFF(forms.ModelForm):
	
	def __init__(self, region, *args, **kwargs):
		super(FormularioCCFF, self).__init__(*args, **kwargs)
		self.fields["inspectores"].queryset = Usuario.objects.filter(region=region)

	class Meta:
		model = ControlesFronterizos
		exclude = ("region",)
		

class FormularioDia(forms.ModelForm):
	
	class Meta:
		model = Dia_CCFF_Terrestre
