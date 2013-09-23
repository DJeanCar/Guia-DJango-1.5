from django.conf.urls import patterns, include, url
from .views import RegistrarAutor,ReportarAutor


urlpatterns = patterns('',
    
    url(r'^registrar/$' , RegistrarAutor.as_view() , name="registrar_autor"),
    url(r'^reportar/$' , ReportarAutor.as_view() , name="reportar_autor"),

)
