# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.cl.cl_regions import REGION_CHOICES
from controles.opciones import *
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

	class Meta:
		verbose_name_plural = "Controles Fronterizos"

		
class Dia(models.Model):
	'''
	Modelo base para los 3 tipos de controles, contiene sólo los campos necesarios
	que se comparten, estos son pasajeros y cites, Dia_CCFF_Terrestre, Dia_CCFF_Maritimo
	y Dia_CCFF_Aereo tienen los medios de transporte de cada tipo de control
	'''
	fecha = models.DateField()
	inspector = models.OneToOneField(User)
	#pasajeros
	hombres_ingresados = models.IntegerField()
	hombres_inspeccionados = models.IntegerField()
	mujeres_ingresadas = models.IntegerField()
	mujeres_inspeccionadas = models.IntegerField()
	declaran_no_si_traen = models.IntegerField()
	declaran_si_si_traen = models.IntegerField()
	declaran_no_no_traen = models.IntegerField()
	n_declaran = models.IntegerField()
	n_adc = models.IntegerField()
	#cites
	cites_entrada_flora = models.IntegerField()
	cites_entrada_fauna = models.IntegerField()
	cites_salida_flora = models.IntegerField()
	cites_salida_fauna = models.IntegerField()


class Dia_CCFF_Terrestre(Dia):

	#medios de transporte
	control_fronterizo = models.ForeignKey(ControlesFronterizos)
	bicicletas_ingresadas = models.IntegerField()
	bicicletas_inspeccionadas = models.IntegerField()
	vehiculo_part_ingresado = models.IntegerField()
	vehiculo_part_inspeccionado = models.IntegerField()
	moto_ingresada = models.IntegerField()
	moto_inspeccionada = models.IntegerField()
	bus_ingresado = models.IntegerField()
	bus_inspeccionado = models.IntegerField()
	tren_pas_ingresado = models.IntegerField()
	tren_pas_inspeccionado = models.IntegerField()
	vehiculo_dipl_ingresado = models.IntegerField()
	vehiculo_dipl_inspeccionado = models.IntegerField()
	vehiculo_hum_ingresado = models.IntegerField()
	vehiculo_hum_inspeccionado = models.IntegerField()
	camion_atingente_ingresado = models.IntegerField()
	camion_atingente_inspeccionado = models.IntegerField()
	camion_no_atingente_ingresado = models.IntegerField()
	camion_no_atingente_inspeccionado = models.IntegerField()
	tren_carga_ingresado = models.IntegerField()
	tren_carga_inspeccionado = models.IntegerField()
	camion_ffaa_at_ingresado = models.IntegerField()
	camion_ffaa_at_inspeccionado = models.IntegerField()
	camion_ffaa_no_at_ingresado = models.IntegerField()
	camion_ffaa_no_at_inspeccionado = models.IntegerField()
	auto_ffaa_ingresado = models.IntegerField()
	auto_ffaa_inspeccionado = models.IntegerField()
	bus_ffaa_ingresado = models.IntegerField()
	bus_ffaa_inspeccionado = models.IntegerField()

	def __unicode__(self):
		return self.fecha


class Dia_CCFF_Maritimo(Dia):

	control_fronterizo = models.ForeignKey(ControlesFronterizos)
	crucero_ingresado = models.IntegerField()
	crucero_inspeccionado = models.IntegerField()
	mercante_ingresado = models.IntegerField()
	mercante_inspeccionado = models.IntegerField()
	contenedor_ingresado = models.IntegerField()
	contenedor_inspeccionado = models.IntegerField()
	cisterna_ingresado = models.IntegerField()
	cisterna_inspeccionado = models.IntegerField()
	tanque_ffaa_ingresado = models.IntegerField()
	tanque_ffaa_inspeccionado = models.IntegerField()
	instruccion_ffaa_ingresado = models.IntegerField()
	instruccion_ffaa_inspeccionado = models.IntegerField()
	guerra_ffaa_ingresado = models.IntegerField()
	guerra_ffaa_inspeccionado = models.IntegerField()
	pas_carga_ffaa_ingresado = models.IntegerField()
	pas_carga_ffaa_inspeccionado = models.IntegerField()
	aviso_recalada_inicio = models.IntegerField()
	aviso_recalada_termino = models.IntegerField()
	acta_recepcion = models.ForeignKey(Actas_Recepcion)
	post_recepcion = models.ForeignKey(Actas_Post_Recepcion)
	
	def __unicode__(self):
		return self.fecha


class Dia_CCFF_Aereo(Dia):

	control_fronterizo = models.ForeignKey(ControlesFronterizos)
	avioneta_ingresada = models.IntegerField()
	avioneta_inspeccionada = models.IntegerField()
	avion_ingresado = models.IntegerField()
	avion_inspeccionado = models.IntegerField()
	heli_ingresado = models.IntegerField()
	heli_inspeccionado = models.IntegerField()
	avion_carga_ingresado = models.IntegerField()
	avion_carga_inspeccionado = models.IntegerField()
	avion_carga_ffaa_ingresado = models.IntegerField()
	avion_carga_ffaa_inspeccionado = models.IntegerField()
	avion_pas_ffaa_ingresado = models.IntegerField()
	avion_pas_ffaa_inspeccionado = models.IntegerField()
	avioneta_ffaa_ingresada = models.IntegerField()
	avioneta_ffaa_inspeccionada = models.IntegerField()
	heli_ffaa_ingresado = models.IntegerField()
	heli_ffaa_inspeccionado = models.IntegerField()
	solicitud_inspeccion = models.ForeignKey(Sol_Inspeccion)
	acta_inspeccion = models.ForeignKey(Actas_Inspeccion)

	def __unicode__(self):
		return self.fecha


class Acta_Nave(models.Model)

	numero = models.IntegerField()
	puerto_inspeccion = models.CharField(max_length=30,choices=puertos)
	nombre_nave = models.CharField(max_length=30)
	agencia = models.CharField(max_length=20)
	puerto_anterior = models.CharField(max_length=20)
	puerto_siguiente = models.CharField(max_length=20)
	arribo = models.DateTimeField()
	recepcion = models.DateTimeField()
	zarpe = models.DateTimeField()
	mujeres_desembarcan = models.IntegerField()
	hombres_desembarcan = models.IntegerField()
	desembarcos = models.ForeignKey(Desembarco_Barco)
	numero_sellos = models.IntegerField()
	ubicacion_sellos = models.CharField(max_length=50)
	sitio_atraque = models.CharField(max_length=20)
	puerto_c_limantria = models.CharField(max_length=20)
	solicitan_antecedentes = models.BooleanField()
	observaciones = models.TextField()
	basuras_tapadas = models.BooleanField()
	basuras_fijas = models.BooleanField()
	basuras_hermeticas = models.BooleanField()
	deficiencia_corregida = models.BooleanField()
	area_no_inspeccionada = models.CharField(max_length=10,choices=areas_no_inspeccionadas)
	animal_a_bordo = models.BooleanField()
	tipo_animal = models.CharField(max_length=20)
	numero_animal = models.IntegerField()
	productos_regulados = models.ManyToManyField(prod_regulados)


class Acta_Recepcion(Acta_Nave)

	pasajeros_ingresan = models.IntegerField()
	descensos = models.IntegerField()
	revision_listado_puertos = models.BooleanField()
	periodo_revision = models.CharField(max_length=15)
	cert_fitosanitario = models.BooleanField()

	def __unicode__(self):
		return self.numero


class Acta_PostRecepcion(Acta_Nave):

	monitoreo = models.BooleanField()
	prod_sellados_recepcion = models.BooleanField()
	mantiene_sellos = models.BooleanField()
	sellos_rotos = models.TextField()
	desembarco_basuras = models.BooleanField()
	transbordo_basuras = models.BooleanField()
	supervision_sag = models.BooleanField()
	adc = models.BooleanField()
	motivo_adc = models.TextField()

	def __unicode__(self):
		return self.numero
class Desembarco_Barco(models.Model):

	fecha = models.DateTimeField()


class Prod_Regulado(models.Model):

	producto = models.CharField()
	kilogramos = models.DecimalField(max_digits=5,decimal_places=2)
	pais_origen = CountryField()
	medida_adoptada = models.CharField(max_length=20)
	numero_muestra = models.IntegerField()
	unidad_muestra = models.CharField(max_length=10)


class Pasajero(models.Model):

	fecha = models.DateField(blank=False)
	inspector = models.ForeignKey(User,blank=False)
	tipo_doc = models.CharField(max_length=19,choices=tipos_documentos,blank=False)
	n_doc = models.CharField(max_length=15,blank=False)
	nombres_apellidos = models.CharField(max_length=40,blank=False)
	genero = models.CharField(max_length=9,choices=opciones_genero)
	declara = models.BooleanField()
	proceso = models.BooleanField()
	pais_origen = CountryField()
	ubicacion = models.CharField(max_length=28)
	ultimo_puerto = models.CharField(max_length=30,choices=puertos)
	prox_puerto = models.CharField(max_length=30,choices=puertos)


class Productos_interceptados(models.Model):
	
	rubro = models.CharField(max_length=8,choices=rubros)
	estado = models.CharField(max_length=6,choices=estados)
	cantidad = models.IntegerField()
	kilos = models.FloatField()
	rip = models.BooleanField()
	kilos_rip = models.FloatField()
	medida_int = models.CharField(max_length=21,choices=medidas_intercepcion)
	comentario_int = models.TextField()


class Intercepcion(Productos_interceptados):

	pasajero = models.ForeignKey("Pasajero")


class Abandono(Productos_interceptados):

	dia = models.DateField()
	inspector = models.ForeignKey(User,blank=False)
	probable_origen = CountryField()
	ubicacion = models.CharField(max_length=28)

'''
class Turno(models.Model):

	inicio = models.DateField()
	fin = models.DateField()
	hora_fin = models.TimeField()
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
'''