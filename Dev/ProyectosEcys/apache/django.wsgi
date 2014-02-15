import os
import sys

path = '/var/www/dev.proyectos-ecys.tk/ProyectosEcys'
if path not in sys.path:
    sys.path.insert(0, '/var/www/dev.proyectos-ecys.tk/ProyectosEcys')

os.environ['DJANGO_SETTINGS_MODULE'] = 'ProyectosEcys.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
