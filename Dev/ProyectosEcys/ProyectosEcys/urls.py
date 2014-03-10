''' modulo encargado del direccionamiento de las url'''
from django.conf.urls import patterns, include, url
from django.contrib import admin
import sistema_pe.urls
admin.autodiscover()

urlpatterns = patterns(
    '',
    #url(r'^$', 'ProyectosEcys.views.home', name='home'),
    url(r'^', include(sistema_pe.urls, namespace='sistema_pe')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/$', include('sistema_pe.urls', namespace='sistema_pe')),
    #url(r'^usuario/', include('sistema_pe.urls', namespace='sistema_pe'))
)
