# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from controles.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^ingreso/$', TemplateView.as_view(template_name='ingreso.html'), name="ingreso"),
	url(r'^$', ingresar, name='home'),
	url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'geoffroea.views.home', name='home'),
    # url(r'^geoffroea/', include('geoffroea.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
