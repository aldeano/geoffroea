# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django_localflavor_cl.cl_regions import REGION_CHOICES
from django_countries import CountryField
from .opciones import *


class TipoUsuario(models.Model):

	usuario = models.OneToOneField(User, unique=True)
	nombre = models.CharField(max_length=40, blank=False)
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

	class Meta:
		abstract = True


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


class Prod_Regulado(models.Model):

	producto = models.CharField(max_length=30)
	kilogramos = models.DecimalField(max_digits=5,decimal_places=2)
	pais_origen = CountryField()
	medida_adoptada = models.CharField(max_length=20)
	numero_muestra = models.IntegerField()
	unidad_muestra = models.CharField(max_length=10)

	def __unicode__(self):
		return self.producto


class Desembarco_Barco(models.Model):

	fecha = models.DateTimeField()


class Acta_Nave(models.Model):

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
	productos_regulados = models.ManyToManyField(Prod_Regulado)

	class Meta:
		abstract = True


class Acta_Recepcion(Acta_Nave):

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
	acta_recepcion = models.ForeignKey(Acta_Recepcion)
	post_recepcion = models.ForeignKey(Acta_PostRecepcion)
	
	def __unicode__(self):
		return self.fecha


class Acta_Aeronave(models.Model):

	numero = models.IntegerField()
	compania_aerea= models.CharField(max_length=30)
	vuelo = models.CharField(max_length=10)
	matricula = models.CharField(max_length=10)
	origen = models.CharField(max_length=20)
	ruta = models.CharField(max_length=50)
	fecha = models.DateField()
	hora_estimada = models.TimeField()
	tipo_vuelo = models.CharField(choices=tipos_vuelo,max_length=9)
	observaciones = models.TextField()

	def __unicode__(self):
		return self.numero

	class Meta:
		abstract = True


class Acta_Inspeccion(Acta_Aeronave):

	nombre_aeropuerto = models.CharField(max_length=30)

	def __unicode__(self):
		return self.numero


class Sol_Inspeccion(Acta_Aeronave):

	escala_uno = models.CharField(max_length=30)
	escala_dos = models.CharField(max_length=30)

	def __unicode__(self):
		return self.numero


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
	acta_inspeccion = models.ForeignKey(Acta_Inspeccion)

	def __unicode__(self):
		return self.fecha


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


class Prod_Interceptable(models.Model):

	categoria = models.CharField(max_length=8)
	subtipo = models.CharField(max_length=30)
	tipo = models.CharField(max_length=30)

	def __unicode__(self):
		return self.tipo


class Record_Intercepcion(models.Model):

	kilos = models.FloatField()
	folio_protocolo = models.IntegerField()

	def __unicode__(self):
		return self.folio_protocolo


class Productos_Interceptados(models.Model):
	
	numero = models.IntegerField()
	intercepcion = models.ManyToManyField(Prod_Interceptable)
	estado = models.CharField(max_length=6,choices=estados)
	cantidad = models.IntegerField()
	kilos = models.FloatField()
	rip = models.OneToOneField(Record_Intercepcion)
	medida_int = models.CharField(max_length=21,choices=medidas_intercepcion)
	comentario_int = models.TextField()

	class Meta:
		abstract = True


class Intercepcion(Productos_Interceptados):

	pasajero = models.ForeignKey(Pasajero)

	def __unicode__(self):
		return self.numero


class Abandono(Productos_Interceptados):

	dia = models.DateField()
	inspector = models.ForeignKey(TipoUsuario, blank=False, related_name="+")
	probable_origen = CountryField()
	ubicacion = models.CharField(max_length=28)

	def __unicode__(self):
		return self.numero


class Orden_Tratamiento(models.Model):

	numero = models.IntegerField()
	fecha = models.DateField()

	def __unicode__(self):
		return self.numero


class Cores(models.Model):

	numero = models.IntegerField()
	fecha = models.DateField()

	def __unicode__(self):
		return self.numero


class Turno(models.Model):

	jefe_turno = models.ForeignKey(TipoUsuario, related_name='+')
	sgte_jefe_turno = models.ForeignKey(TipoUsuario, related_name='+')
	dia_entrega = models.DateTimeField()
	llenado_furi = models.CharField(max_length=3,choices=opciones_llenado)
	obs_llenado = models.CharField(max_length=80)
	deteccion_prod_no_conf = models.CharField(max_length=3,choices=opciones_llenado)
	obs_deteccion = models.CharField(max_length=80)
	intercepcion_ampliada  = models.CharField(max_length=3,choices=opciones_llenado)
	obs_intercepcion = models.CharField(max_length=80)
	proc_administrativo = models.CharField(max_length=3,choices=opciones_llenado)
	obs_proc_admin = models.CharField(max_length=80)
	funcionamiento_rx = models.CharField(max_length=3,choices=opciones_llenado)
	obs_func_rx = models.CharField(max_length=80)
	funcionamiento_canina = models.CharField(max_length=3,choices=opciones_llenado)
	obs_func_canina = models.CharField(max_length=80)
	funcionamiento_incin = models.CharField(max_length=3,choices=opciones_llenado)
	obs_func_incin = models.CharField(max_length=80)
	envio_reclamos = models.CharField(max_length=3,choices=opciones_llenado)
	obs_reclamos = models.CharField(max_length=80)
	prod_no_eliminados = models.CharField(max_length=3,choices=opciones_llenado)
	obs_no_eliminados = models.CharField(max_length=80)
	recepcion_correos = models.CharField(max_length=3,choices=opciones_llenado)
	obs_recepcion = models.CharField(max_length=80)
	envios_adc = models.CharField(max_length=3,choices=opciones_llenado)
	obs_adc = models.CharField(max_length=80)
	envio_cites = models.CharField(max_length=3,choices=opciones_llenado)
	obs_cites = models.CharField(max_length=80)
	envio_ac_incidentes = models.CharField(max_length=3,choices=opciones_llenado)
	obs_incidentes = models.CharField(max_length=80)
	deteccion_ingreso = models.CharField(max_length=3,choices=opciones_llenado)
	obs_ingreso = models.CharField(max_length=80)
	inspectores = models.ManyToManyField(TipoUsuario, related_name='+')


class Acta_Intercepcion(models.Model):
	
	numero = models.IntegerField(unique=True,blank=False)
	intercepcion = models.ForeignKey(Intercepcion)
	inspector = models.ForeignKey(TipoUsuario)
	firma = models.BooleanField()

	def __unicode__(self):
		return self.numero


class Acta_Retencion(models.Model):

	numero = models.IntegerField(unique=True,blank=False)
	intercepcion = models.ForeignKey(Intercepcion)
	motivo = models.CharField(max_length=50)
	desde = models.DateField()
	hasta = models.DateField()
	lugar = models.CharField(max_length=50)
	tipo_envase = models.CharField(max_length=50)
	observaciones = models.TextField()

	def __unicode__(self):
		return self.numero


class Acta_Destruccion(models.Model):

	numero = models.IntegerField(unique=True,blank=False)
	intercepcion = models.ForeignKey(Intercepcion)
	inspector = models.ForeignKey(TipoUsuario)
	firma = models.BooleanField()
	acta_intercepcion = models.ForeignKey(Acta_Intercepcion)
	acta_retencion = models.ForeignKey(Acta_Retencion)
	resolucion = models.CharField(max_length=15)
	desnaturalizacion = models.BooleanField()
	prod_desnaturalizacion = models.CharField(max_length=15)
	observaciones = models.TextField()

	def __unicode__(self):
		return self.numero


class Acta_Denuncia_Citacion(models.Model):

	numero = models.IntegerField(unique=True,blank=False)
	infractor = models.ForeignKey(Pasajero, related_name="infractor_adc")
	hechos = models.TextField()
	observaciones = models.TextField()
	acta_retencion = models.ForeignKey(Acta_Retencion,blank=True)
	oficina_citacion = models.CharField(max_length=30)
	hora_citacion = models.DateTimeField()
	firma = models.BooleanField()

	def __unicode__(self):
		return self.numero


class Acta_Incidente(models.Model):

	numero = models.IntegerField(unique=True,blank=False)
	pasajero = models.ForeignKey(Pasajero, related_name="pasajero_ai")
	incidente = models.TextField()
	observaciones = models.TextField()
	firma = models.BooleanField()

	def __unicode__(self):
		return self.numero


class Especimen_Cites(models.Model):

	nombre_comun = models.CharField(max_length=30)
	nombre_cientifico = models.CharField(max_length=30)
	cantidad = models.IntegerField()
	pais_procedencia = models.CharField(max_length=30)
	acta_intercepcion = models.ForeignKey(Acta_Intercepcion)
	estado_especimen = models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre_comun


class Acta_Devolucion_Cites(models.Model):

	numero = models.IntegerField(unique=True,blank=False)
	fecha_devolucion = models.DateField()
	especimen = models.ForeignKey(Especimen_Cites, related_name="+")
	tenedor = models.ForeignKey(Pasajero, related_name="tenedor_adci")
	causal = models.TextField()
	receptor = models.CharField(max_length=50)
	cargo_receptor = models.CharField(max_length=20)
	institucion_receptor = models.CharField(max_length=20)

	def __unicode__(self):
		return self.numero
