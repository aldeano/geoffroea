from django.db import models
from django.contrib.auth.models import User

class TipoUsuario(models.Model):

	tipos_usuarios = (
		(admin, "Administrador"),
		(er, "Encargado(a) Regional"),
		(jf, "Jefe(a) de Turno"),
		(inspector, "Inspector")
		)

	usuario = models.OneToOneField(User)
	tipo = models.CharField(choices=tipos_usuarios)
