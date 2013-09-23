from django.views.generic import CreateView,TemplateView,ListView
from .models import Autor
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext

class RegistrarAutor(CreateView):
	template_name = 'autores/registrarAutor.html'
	model = Autor
	success_url = reverse_lazy('reportar_autor')

	

class ReportarAutor(ListView):
	template_name = 'autores/reportarAutor.html'
	model = Autor
	context_object_name = 'autores'



