from django.views.generic import TemplateView,FormView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from .models import Perfiles


class Registrarse(FormView):
	template_name = 'inicio/registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')

	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.usuario = user
		perfil.telefono = form.cleaned_data['telefono']
		perfil.save()
		return super(Registrarse , self).form_valid(form)
	
	

