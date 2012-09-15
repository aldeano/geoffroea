from django.db import models
from django.contrib.auth.models import User

class TipoUsuario(models.Model):

	tipos_usuarios = (
		("adm", "Administrador"),
		("er", "Encargado(a) Regional"),
		("jf", "Jefe(a) de Turno"),
		("insp", "Inspector")
		)

	usuario = models.OneToOneField(User, unique=True)
	tipo = models.CharField(choices=tipos_usuarios,max_length=4)
