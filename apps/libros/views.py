from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Libro
from apps.autores.models import Autor


class BuscarView(TemplateView):
	

	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscalo']
		libros = Libro.objects.filter(nombre__contains=buscar)
		if libros:
			datos = []
			for libro in libros:
				autores = libro.autor.all()
				datos.append(dict([(libro,autores)]))
			return render(request,'libros/buscar.html',
					 {'datos':datos})
		else:
			autores = Autor.objects.filter(nombre__contains=buscar)
			return render(request, 'libros/buscar.html',
						{'autores':autores , 'autor':True})