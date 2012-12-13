# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.cl.cl_regions import REGION_CHOICES
from controles.comunas import comunas
from django_countries import CountryField

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


class Dia(models.Model):
	'''
	Modelo base para los 3 tipos de controles, contiene sólo los campos necesarios
	que se comparten, estos son pasajeros y cites, Dia_CCFF_Terrestre, Dia_CCFF_Maritimo
	y Dia_CCFF_Aereo tienen los medios de transporte de cada tipo de control
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


class Dia_CCFF_Terrestre(Dia)

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

	def __unicode__(self):
		return self.fecha


class Dia_CCFF_Maritimo(Dia):

	crucero_ingresado = models.IntegerField(max_digits=3)
	crucero_inspeccionado = models.IntegerField(max_digits=3)
	mercante_ingresado = models.IntegerField(max_digits=3)
	mercante_inspeccionado = models.IntegerField(max_digits=3)
	contenedor_ingresado = models.IntegerField(max_digits=3)
	contenedor_inspeccionado = models.IntegerField(max_digits=3)
	cisterna_ingresado = models.IntegerField(max_digits=3)
	cisterna_inspeccionado = models.IntegerField(max_digits=3)
	tanque_ffaa_ingresado = models.IntegerField(max_digits=3)
	tanque_ffaa_inspeccionado = models.IntegerField(max_digits=3)
	instruccion_ffaa_ingresado = models.IntegerField(max_digits=3)
	instruccion_ffaa_inspeccionado = models.IntegerField(max_digits=3)
	guerra_ffaa_ingresado = models.IntegerField(max_digits=3)
	guerra_ffaa_inspeccionado = models.IntegerField(max_digits=3)
	pas_carga_ffaa_ingresado = models.IntegerField(max_digits=3)
	pas_carga_ffaa_inspeccionado = models.IntegerField(max_digits=3)

	def __unicode__(self):
		return self.fecha


class Dia_CCFF_Aereo(dia):

	avioneta_ingresada = models.IntegerField(max_digits=3)
	avioneta_inspeccionada = models.IntegerField(max_digits=3)
	avion_ingresado = models.IntegerField(max_digits=3)
	avion_inspeccionado = models.IntegerField(max_digits=3)
	heli_ingresado = models.IntegerField(max_digits=3)
	heli_inspeccionado = models.IntegerField(max_digits=3)
	avion_carga_ingresado = models.IntegerField(max_digits=3)
	avion_carga_inspeccionado = models.IntegerField(max_digits=3)
	avion_carga_ffaa_ingresado = models.IntegerField(max_digits=3)
	avion_carga_ffaa_inspeccionado = models.IntegerField(max_digits=3)
	avion_pas_ffaa_ingresado = models.IntegerField(max_digits=3)
	avion_pas_ffaa_inspeccionado = models.IntegerField(max_digits=3)
	avioneta_ffaa_ingresada = models.IntegerField(max_digits=3)
	avioneta_ffaa_inspeccionada = models.IntegerField(max_digits=3)
	heli_ffaa_ingresado = models.IntegerField(max_digits=3)
	heli_ffaa_inspeccionado = models.IntegerField(max_digits=3)

	def __unicode__(self):
		return self.fecha


class Pasajero(models.Model):

	fecha = models.DateField(blank=False)
	inspector = models.ForeignKey(User,blank=False)
	tipo_doc = models.CharField(choices=tipos_documentos,blank=False)
	n_doc = models.CharField(max_length=15,blank=False)
	nombres_apellidos = models.CharField(max_length=40,blank=False)
	genero = models.CharField(choices=opciones_genero)
	declara = models.BooleanField()
	proceso = models.BooleanField()
	pais_origen = CountryField()
	ubicacion = models.CharField()
	ultimo_puerto = models.CharField(choices=puertos)
	prox_puerto = models.CharField(choices=puertos)


class Productos_interceptados(models.Model):
	
	rubro = models.CharField(choices=rubros)
	estado = models.CharField(choices=estados)
	cantidad = models.IntegerField()
	kilos = models.FloatField()
	rip = models.BooleanField()
	kilos_rip = models.FloatField()
	medida_int = models.CharField(choices=medidas_intercepcion)
	comentario_int = models.TextField()

class Intercepcion(Productos_interceptados):

	pasajero = models.ForeignKey("Pasajero")


class Abandono(Productos_interceptados):

	dia = models.DateField()
	inspector = models.ForeignKey(User,blank=False)
	probable_origen = CountryField()
	ubicacion = models.CharField()


class Turno(models.Model):

	inicio = models.DateField()
	fin = models.DateField()
	cores = models.CharField()
	quemas = models.ManyToManyField(Quema)


class Quema(models.Model):

	dia = models.DateField()
	rdi = models.ManyToManyField(Dia)
	control = models.ManyToManyField(ControlesFronterizos)


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
	resolucion = models.CharField(max_length=15)
	prod_interceptado = models.ManyToManyField("Intercepciones")
	desnaturalizacion = models.BooleanField(blank=False)
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
