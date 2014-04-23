# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('',
	url(r'^ccff/$', login_required(ListarCCFF.as_view()), name="listar_ccff"),
	url(r'^detalles_ccff/$', login_required(DetallesCCFF.as_view()), name="detalles_ccff"),
    url(r'^agregar_ccff/$', login_required(AgregarCCFF.as_view()), name="agregar_ccff"),
    url(r'^borrar_ccff/$', login_required(BorrarCCFF.as_view()), name="borrar_ccff"),
    url(r'^modificar_ccff/$', login_required(ModificarCCFF.as_view()), name="modificar_ccff"),
    url(r'^insp/$', login_required(ListarInspector.as_view()), name="listar_insp"),
    url(r'^detalles_insp/$', login_required(DetallesInspector.as_view()), name="detalles_insp"),
    url(r'^agregar_insp/$', login_required(AgregarInspector.as_view()), name="agregar_insp"),
    url(r'^borrar_insp/$', login_required(BorrarInspector.as_view()), name="borrar_insp"),
    url(r'^modificar_insp/$', login_required(ModificarInspector.as_view()), name="modificar_insp"),
    url(r'^$', login_required(GestionRegistros.as_view()), name="gestion_registros"),
    )
