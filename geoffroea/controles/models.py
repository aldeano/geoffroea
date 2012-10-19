# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.cl.cl_regions import REGION_CHOICES
from controles.comunas import comunas

class TipoUsuario(models.Model):

	tipos_usuarios = (
		("adm", "Administrador"),
		("er", "Encargado(a) Regional"),
		("jf", "Jefe(a) de Turno"),
		("insp", "Inspector")
		)

	usuario = models.OneToOneField(User, unique=True)
	tipo = models.CharField(choices=tipos_usuarios,max_length=4,blank=False)
	region = models.CharField(choices=REGION_CHOICES,max_length=55,blank=False)

	def __unicode__(self):
		return self.tipo

class ControlesFronterizos(models.Model):

	horarios_ccff = (
		("continuado", "continuado"),
		("turnos", "turnos"),
		("esporadico", "esporádico")
		)

	nombre = models.CharField(unique=True, max_length=30)
	region = models.CharField(choices=REGION_CHOICES,max_length=55,blank=False)
	inspectores = models.ManyToManyField(User,null=True)
	latitud = models.DecimalField(max_digits=11,decimal_places=8)
	longitud = models.DecimalField(max_digits=11,decimal_places=8)
	turno = models.CharField(choices=horarios_ccff,max_length=12)
	horario_inicio = models.TimeField(null=True)
	horario_termino = models.TimeField(null=True)
	comuna = models.CharField(choices=comunas,max_length=25)

	def __unicode__(self):
		return self.nombre

class Turno(models.Model):

	inicio = models.DateField()
	fin = models.DateField()
	cores = models.CharField()
	quemas = models.ManyToManyField(Quema)

class Quema(models.Model):

	dia = models.DateField()
	rdi = models.ManyToManyField(Dia)
	control = models.ManyToManyField(ControlesFronterizos)

class Dia(models.Model):
	pass

class Intercepciones(models.Model):
	pass
