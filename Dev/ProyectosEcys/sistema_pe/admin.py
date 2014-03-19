from django.contrib import admin
from sistema_pe.models import Usuario
from sistema_pe.models import Clase
from sistema_pe.models import Repositorio

from sistema_pe.models import Semestre
from sistema_pe.models import Proyecto
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Clase)
admin.site.register(Proyecto)
admin.site.register(Repositorio)
admin.site.register(Semestre)
