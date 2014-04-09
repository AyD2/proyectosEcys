''' Modulo encargado del direccionamiento de las url que bienen desde
    ProyectoEcys.urls.py'''
from django.conf.urls import patterns, url
import sistema_pe.views

urlpatterns = patterns(
    '',
    url(r'^$', sistema_pe.views.index, name='usuario'),
    url(r'^login/$', sistema_pe.views.login, name='index'),
    url(r'^perfil/$', sistema_pe.views.perfil, name='perfil'),
    #url(r'^tutor/$', sistema_pe.views.tutor, name='tutor'),
    url(r'^logout/$', sistema_pe.views.logout, name='logout'),
)
