# -*- coding: utf-8 -*-
"""
uso: python manage.py test controles
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from controles.models import *

class ControlTest(TestCase):

    pass

    def test_urls_correctas(self):
        
        urls_correctas  = (reverse("inicio"))
        
        for url in urls_correctas:
            respuesta = self.client.get(url)
            self.assertEqual(respuesta.status_code, 200)
    
    # def test_urls_incorrectas(self):
        
    #     urls_incorrectas = ("/sdfdsg")
        
    #     for url in urls_incorrectas:
    #         respuesta = self.client.get(url)
    #         self.assertEqual(respuesta.status_code, 404)

class ModelosTest(TestCase):

    def test_permisos(self):
        self.u1 = User.objects.create(username="Administrador")
        self.up1 = TipoUsuario.objects.create(usuario=self.u1,tipo="adm")
        self.assertEqual(self.up1.tipo,"adm")

    def test_ccff(self):
        self.ccff = ControlesFronterizos(
            nombre="Chacalluta",
            region="XV",
            latitud="17.435",
            longitud="32.456",
            turno="continuado",
            comuna="15101",
            )
        self.ccff.save()
        self.ccff.inspectores.create(username="testeador")

        self.assertEqual(self.ccff.turno, "continuado")
        self.assertEqual(self.ccff.comuna, "15101")