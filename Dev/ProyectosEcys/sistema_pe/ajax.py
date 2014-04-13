'''modulo con todas las peticiones ajax'''
from django.utils import simplejson
from django.core import serializers
from dajaxice.decorators import dajaxice_register
from sistema_pe.models import Clase


@dajaxice_register
def traer_repos(request):
    '''obtiene una lista de repositorios para un usuario
    en especifico por medio de su numero de carne'''
    print request
    return simplejson.dumps({'repos':'mierda'})

@dajaxice_register
def traer_cursos(request):
    '''obtiene desde la base de datos una lista con todos
    los cursos registrados en el sistema'''
    print request
    clases = Clase.objects.all()
    return serializers.serialize("json", clases)
