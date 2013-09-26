from django.conf.urls import patterns, include, url
from .views import BuscarView


urlpatterns = patterns('',

	url(r'^buscar/$' , BuscarView.as_view(), name='buscar'),

)
