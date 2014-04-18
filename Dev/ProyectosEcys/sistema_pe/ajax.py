'''modulo con todas las peticiones ajax'''

from django.utils import simplejson
from django.core import serializers
from dajaxice.decorators import dajaxice_register
from sistema_pe.models import Clase, Usuario, Asignacion
import print_log


@dajaxice_register
def traer_repos(request):
    '''obtiene una lista de repositorios para un usuario
    en especifico por medio de su numero de carne'''
    print request
    return None

@dajaxice_register
def traer_cursos(request, carnet):
    '''obtiene desde la base de datos una lista con todos
    los cursos registrados en el sistema'''
    u = Usuario.objects.get(carnet=carnet)
    todas = Clase.objects.all()
    asignacion = Asignacion.objects.filter(id_carnet=u)
    asignadasjson = serializers.serialize("json", asignacion)
    todasjson = serializers.serialize("json", todas)

    asig_lst = simplejson.loads(asignadasjson)
    todas_lst = simplejson.loads(todasjson)

    return simplejson.dumps({'todo': todas_lst, 'asignadas':asig_lst})

@dajaxice_register
def asignar(request, carnet, clase):
    '''asigna una clase a un alumno'''
    u = Usuario.objects.get(carnet=carnet)
    c = Clase.objects.get(pk=clase)
    asig = Asignacion(id_carnet=u, id_Clase=c)
    #asig.save()
    print_log.app_mesaje("se asigno el usuario: "+carnet +"a la clase "+clase)
    todas = Clase.objects.all()
    asignacion = Asignacion.objects.filter(id_carnet=u)
    asignadasjson = serializers.serialize("json", asignacion)
    todasjson = serializers.serialize("json", todas)

    asig_lst = simplejson.loads(asignadasjson)
    todas_lst = simplejson.loads(todasjson)

    return simplejson.dumps({'todo': todas_lst, 'asignadas':asig_lst})
    
