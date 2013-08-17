# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import GestionRegistros, AgregarCCFF, ModificarCCFF, AgregarInspector, ModificarInspector

urlpatterns = patterns('',
    url(r'^agregarccff/$', login_required(AgregarCCFF.as_view()), name="agregar_ccff"),
    url(r'^modificarccff/$', login_required(ModificarCCFF.as_view()), name="modificar_ccff"),
    url(r'^agregar_ins/$', login_required(AgregarInspector.as_view()), name="agregar_ins"),
    url(r'^modificar_ins/$', login_required(ModificarInspector.as_view()), name="modificar_ins"),
    url(r'^$', login_required(GestionRegistros.as_view()), name="gestion_registros"),
    )
