# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from controles.views import PortadaFuri, GestionRegistros

admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^ingreso/$', login_required(GestionRegistros.as_view()), name="ingreso"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', PortadaFuri.as_view(), name="inicio"),
	
    # Examples:
    # url(r'^$', 'geoffroea.views.home', name='home'),
    # url(r'^geoffroea/', include('geoffroea.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
