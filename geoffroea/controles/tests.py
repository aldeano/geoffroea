"""
uso: python manage.py test controles
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from controles.models import TipoUsuario

class ControlTest(TestCase):

    def test_urls_correctas(self):
        
        urls_correctas  = (reverse("home"), reverse("ingreso"))
        
        for url in urls_correctas:
            respuesta = self.client.get(url)
            self.assertEqual(respuesta.status_code, 200)
    
    def test_urls_incorrectas(self):
        
        urls_incorrectas = ("/sdgf/", "/ingreso/dfgtrh/")
        
        for url in urls_incorrectas:
            respuesta = self.client.get(url)
            self.assertEqual(respuesta.status_code, 404)

class UsuariosTest(TestCase):

    def test_permisos(self):
        self.u1 = User.objects.create(username="Administrador")
        self.up1 = TipoUsuario.objects.create(usuario=self.u1,tipo="adm")
