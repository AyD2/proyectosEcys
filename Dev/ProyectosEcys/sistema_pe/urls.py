''' Modulo encargado del direccionamiento de las url que bienen desde
    ProyectoEcys.urls.py'''
from django.conf.urls import patterns, url, include
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import sistema_pe.views

dajaxice_autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', sistema_pe.views.index, name='usuario'),
    url(r'^login/$', sistema_pe.views.login, name='index'),
    url(r'^perfil/$', sistema_pe.views.perfil, name='perfil'),
    #url(r'^tutor/$', sistema_pe.views.tutor, name='tutor'),
    url(r'^logout/$', sistema_pe.views.logout, name='logout'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls'))
)

urlpatterns += staticfiles_urlpatterns()
