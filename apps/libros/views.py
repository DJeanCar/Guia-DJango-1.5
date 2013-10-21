from django.views.generic import TemplateView,ListView
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


class BusquedaView(ListView):
	model = Autor
	template_name = 'libros/busqueda.html'
	context_object_name = 'autores'


from django.core import serializers
from django.http import HttpResponse

class BusquedaAjaxView(TemplateView):

	def get(self, request, *args, **kwargs):
		id_autor = request.GET['id']
		libros = Libro.objects.filter(autor__id=id_autor)
		data = serializers.serialize('json', libros,
					fields=('nombre','resumen'))
		return HttpResponse(data, mimetype='application/json')