''' modulo encargado del direccionamiento de las url'''
from django.conf.urls import patterns, include, url
from django.contrib import admin
import sistema_pe.urls
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

dajaxice_autodiscover()
admin.autodiscover()


urlpatterns = patterns(
    '',
    #url(r'^$', 'ProyectosEcys.views.home', name='home'),
    url(r'^', include(sistema_pe.urls, namespace='sistema_pe')),
    url(r'^admin/', include(admin.site.urls)),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^uploads/$', 'upload')
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
