"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class ControlTest(TestCase):

    def test_urls_correctas(self):
        
		urls_correctas  = ("/", "/ingreso/")
        
		for url in urls_correctas:
			respuesta = self.client.get(url)
			self.assertEqual(respuesta.status_code, 200)
	
	# def test_urls_incorrectas(self):
		
		# urls_incorrectas = ("/sdgf/", "/ingreso/dfgtrh/")
		
		# for url in urls_incorrectas:
			# resp = self.client.page(url)
			# self.assertEqual(respuesta.status_code, 404)