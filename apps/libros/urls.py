from django.conf.urls import patterns, include, url
from .views import BuscarView,BusquedaView,BusquedaAjaxView



urlpatterns = patterns('',

	url(r'^buscar/$' , BuscarView.as_view(), name='buscar'),
	url(r'^busqueda/$', BusquedaView.as_view()),
	url(r'^busqueda_ajax/$', BusquedaAjaxView.as_view()),

)
