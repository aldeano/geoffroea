# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.cl.cl_regions import REGION_CHOICES
from controles.comunas import comunas

class TipoUsuario(models.Model):

	usuario = models.OneToOneField(User, unique=True)
	tipo = models.CharField(choices=tipos_usuarios,max_length=4,blank=False)
	region = models.CharField(choices=REGION_CHOICES,max_length=55,blank=False)

	def __unicode__(self):
		return self.tipo

class ControlesFronterizos(models.Model):

	nombre = models.CharField(unique=True, max_length=30)
	region = models.CharField(choices=REGION_CHOICES,max_length=55,blank=False)
	inspectores = models.ManyToManyField(User,null=True)
	latitud = models.DecimalField(max_digits=11,decimal_places=8)
	longitud = models.DecimalField(max_digits=11,decimal_places=8)
	turno = models.CharField(choices=horarios_ccff,max_length=12)
	horario_inicio = models.TimeField(null=True)
	horario_termino = models.TimeField(null=True)
	comuna = models.CharField(choices=comunas,max_length=25)
	codigo = models.CharField(max_length=8,blank=False)

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
	'''
	Modelo base para los 3 tipos de controles, contiene sólo los campos necesarios
	que se comparten, estos son pasajeros y cites, medios de transporte depende
	de cada tipo de control
	'''
	fecha = models.DateField()
	inspector = models.OneToOneField(User)
	#pasajeros
	hombres_ingresados = models.IntegerField(max_digits=5)
	hombres_inspeccionados = models.IntegerField(max_digits=5)
	mujeres_ingresadas = models.IntegerField(max_digits=5)
	mujeres_inspeccionadas = models.IntegerField(max_digits=5)
	declaran_no_si_traen = models.IntegerField(max_digits=5)
	declaran_si_si_traen = models.IntegerField(max_digits=5)
	declaran_no_no_traen = models.IntegerField(max_digits=5)
	n_declaran = models.IntegerField(max_digits=5)
	n_adc = models.IntegerField(max_digits=2)
	#cites
	cites_entrada_flora = models.IntegerField(max_digits=2)
	cites_entrada_fauna = models.IntegerField(max_digits=2)
	cites_salida_flora = models.IntegerField(max_digits=2)
	cites_salida_fauna = models.IntegerField(max_digits=2)

class Dia_ccff_terrestre(Dia)
	#medios de transporte
	bicicletas_ingresadas = models.IntegerField(max_digits=3)
	bicicletas_inspeccionadas = models.IntegerField(max_digits=3)
	vehiculo_part_ingresado = models.IntegerField(max_digits=3)
	vehiculo_part_inspeccionado = models.IntegerField(max_digits=3)
	moto_ingresada = models.IntegerField(max_digits=3)
	moto_inspeccionada = models.IntegerField(max_digits=3)
	bus_ingresado = models.IntegerField(max_digits=3)
	bus_inspeccionado = models.IntegerField(max_digits=3)
	tren_pas_ingresado = models.IntegerField(max_digits=3)
	tren_pas_inspeccionado = models.IntegerField(max_digits=3)
	vehiculo_dipl_ingresado = models.IntegerField(max_digits=3)
	vehiculo_dipl_inspeccionado = models.IntegerField(max_digits=3)
	vehiculo_hum_ingresado = models.IntegerField(max_digits=3)
	vehiculo_hum_inspeccionado = models.IntegerField(max_digits=3)
	camion_atingente_ingresado = models.IntegerField(max_digits=3)
	camion_atingente_inspeccionado = models.IntegerField(max_digits=3)
	camion_no_atingente_ingresado = models.IntegerField(max_digits=3)
	camion_no_atingente_inspeccionado = models.IntegerField(max_digits=3)
	tren_carga_ingresado = models.IntegerField(max_digits=3)
	tren_carga_inspeccionado = models.IntegerField(max_digits=3)
	camion_ffaa_at_ingresado = models.IntegerField(max_digits=3)
	camion_ffaa_at_inspeccionado = models.IntegerField(max_digits=3)
	camion_ffaa_no_at_ingresado = models.IntegerField(max_digits=3)
	camion_ffaa_no_at_inspeccionado = models.IntegerField(max_digits=3)
	auto_ffaa_ingresado = models.IntegerField(max_digits=3)
	auto_ffaa_inspeccionado = models.IntegerField(max_digits=3)
	bus_ffaa_ingresado = models.IntegerField(max_digits=3)
	bus_ffaa_inspeccionado = models.IntegerField(max_digits=3)

class Pasajero(models.Model):
	fecha = models.DateField()

class Intercepciones(models.Model):
	pasajero = models.ForeignKey("Pasajero")


class Acta_Destruccion(models.Model):
	numero = models.IntegerField(unique=True,blank=False)
	region = models.IntegerField(blank=False)
	codigo_ccff = models.CharField(max_length=8,blank=False)
	fecha = models.DateField(blank=False)
	oficina_sag = models.CharField(max_length=30,blank=False)
	nombre_ccff = models.CharField(max_length=30,blank=False)
	tipo_transporte = models.CharField(choices=tipo_transporte,blank=False)
	acta_intercepcion = models.ManyToManyField("Acta_Intercepcion")
	acta_retencion = models.ManyToManyField("Acta_Retencion")
	resolución = models.CharField(max_length=15)
	prod_interceptado = models.ManyToManyField("Intercepciones")
	desnaturalización = models.Booleanfield(blank=False)
	prod_desnaturalizacion = models.CharField(max_length=40)
	medida_aplicada = models.CharField(choices=medidas_destruccion,blank=False)
	observaciones = models.TextField()

class Acta_Intercepcion(models.Model):
	numero = models.IntegerField(unique=True,blank=False)
	region = models.IntegerField(blank=False)
	codigo_ccff = models.CharField(max_length=8,blank=False)
	fecha = models.DateField(blank=False)
	oficina_sag = models.CharField(max_length=30,blank=False)
	nombres_apellidos =
