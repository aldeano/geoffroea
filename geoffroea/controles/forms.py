# -*- coding: utf-8 -*-
from django import forms
from .models import Usuario, ControlesFronterizos, Dia_CCFF_Terrestre
from opciones import comunas

class FormularioPerfil(forms.ModelForm):
	# estas opciones están fijas porque el formulario sólo se ocupa en el
	# frontend por parte de los encargados regionales, quienes sólo pueden
	# asignar jefes o inspectores.
			
	def __init__(self, *args, **kwargs):
		opciones = (("jf", "Jefe(a) de Turno"),
				("insp", "Inspector(a)"))
		super(FormularioPerfil, self).__init__(*args, **kwargs)
		self.fields["cargo"] = forms.ChoiceField(choices=opciones)
		self.fields["region"].widget = forms.HiddenInput()
		self.fields["clave1"] = forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
		self.fields["clave2"] = forms.CharField(widget=forms.PasswordInput(),label="Repite la contraseña")
	
	def clean_clave2(self):
		clave1 = self.cleaned_data.get("clave1", "")
		clave2 = self.cleaned_data["clave2"]
		if clave1 != clave2:
			raise forms.ValidationError(("las contraseñas no coinciden"))
		return clave2
		
	def save(self, commit=True):
		usuario = super(FormularioPerfil, self).save(commit=False)
		usuario.set_password(self.cleaned_data["clave1"])
		if commit:
			usuario.save()
		return usuario
	
	class Meta:
		model = Usuario
		fields = ("username", "first_name", "last_name", "cargo", "region", "controles")
	
	# Para poder asignar controles a cada usuario, se llama un campo del tipo
	# modelmultiplechoicefield y se le asignan los valores obtenidos del
	# queryset al modelo controlesfronterizos
	
	controles = forms.ModelMultipleChoiceField(
		queryset = ControlesFronterizos.objects.all(),
		required = True,
		)

class ModificacionPerfil(forms.ModelForm):
	# Para modificar aspectos del usuario por el eerr en el frontend
	
	class Meta:
		model = Usuario
		fields = ("cargo",)

class FormularioCCFF(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		usuario = kwargs.pop("usuario")
		super(FormularioCCFF, self).__init__(*args, **kwargs)
		self.fields["inspectores"].queryset = Usuario.objects.filter(region=usuario.region).exclude(username=usuario.username)
		self.fields["comuna"] = forms.ChoiceField(choices=comunas[usuario.get_region_display()])
	
	def clean(self):
		if self.cleaned_data.get('turno') == "turnos":
			if self.cleaned_data.get('horario_inicio') == False:
				raise ValidationError(
					u"Si el control funciona en turnos debes asignar horario de inicio"
				)
			elif self.cleaned_data.get('horario_termino') == False:
				raise ValidationError(
					u"Si el control funciona en turnos debes asignar horario de término"
				)
				
		return self.cleaned_data

	class Meta:
		model = ControlesFronterizos
		exclude = ("region", "slug")
		

class FormularioDia(forms.ModelForm):
	
	class Meta:
		model = Dia_CCFF_Terrestre
