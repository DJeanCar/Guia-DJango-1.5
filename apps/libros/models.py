from django.db import models
from apps.autores.models import Autor

class Libro(models.Model):
	autor = models.ManyToManyField(Autor)
	nombre = models.CharField(max_length=50)
	resumen = models.TextField(max_length=300)
	portadas = models.ImageField(upload_to = 'portadas')

	def __unicode__(self):
		return self.nombre

	def traer_url_portadas(self):
		return 'http://localhost:8000/media/%s' % self.portadas


	