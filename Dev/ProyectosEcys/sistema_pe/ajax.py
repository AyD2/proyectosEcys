'''modulo con todas las peticiones ajax'''
from django.utils import simplejson
from django.core import serializers
from dajaxice.decorators import dajaxice_register
from sistema_pe.models import Clase, Usuario, Asignacion, Repositorio
import hashlib
import os


@dajaxice_register
def traer_repos(request, carnet):
    '''obtiene una lista de repositorios para un usuario
    en especifico por medio de su numero de carne'''
    carnet = int(carnet)
    usuario = Usuario.objects.get(carnet=carnet)
    clase = Clase.objects.filter(activa=True)
    asignaciones = Asignacion.objects.filter(id_carnet=usuario, id_Clase=clase)
    print request
    return None

@dajaxice_register
def traer_cursos(request, carnet):
    '''obtiene desde la base de datos una lista con todos
    los cursos registrados en el sistema'''
    #print request
    return listas_de_cursos(carnet)

@dajaxice_register
def asignar_curso(request, datos):
    '''asigna una clase a un alumno'''
    #print request
    carnet = int(datos[0])
    clase = int(datos[1])
    u = Usuario.objects.get(carnet=carnet)
    c = Clase.objects.get(pk=clase)
    asig = Asignacion(id_carnet=u, id_Clase=c)
    asig.save()
    return listas_de_cursos(carnet)

@dajaxice_register
def desasignar_curso(request, datos):
    carnet = datos[0]
    asignacion = datos[1]
    Asignacion.objects.get(pk=asignacion).delete()
    return listas_de_cursos(carnet)

@dajaxice_register
def cambiar_pass(request, datos):
    carnet = int(datos[0])
    passn = datos[1]
    passa = datos[2]
    texto = ""
    u = Usuario.objects.get(carnet=carnet)
    passdeco = hashlib.sha512(passa).hexdigest()
    passndeco = hashlib.sha512(passn).hexdigest()
    if (u.clave == passdeco):
        u.clave = passndeco
        u.save()
        texto = "cambio realizado exitosamente"
    else:
        texto = "el cambio no se pudo realizar"
        print 'algo'

    return simplejson.dumps({'texto': texto })

@dajaxice_register
def cambiar_correo(request, datos):
    carnet = int(datos[0])
    correo = datos[1]
    passa = datos[2]
    texto = ""
    u = Usuario.objects.get(carnet=carnet)
    passdeco = hashlib.sha512(passa).hexdigest()
    if (u.clave == passdeco):
        u.correo = correo 
        u.save()
        texto = "cambio realizado exitosamente"
    else:
        texto = "el cambio no se pudo realizar"
        print 'algo'

    return simplejson.dumps({'texto': texto })

#generales
def listas_de_cursos(carnet):
    #arch = open('prueba.txt','w')
    #arch.write(os.popen('pwd').readline())
    #arch.close() 
    #arch = open('/home/ojr/prueba.txt', 'w')
    #arch.write("algo")
    #arch.close()
    u = Usuario.objects.get(carnet=carnet)
    todas = Clase.objects.filter(activa=True)
    asignacion = Asignacion.objects.filter(id_carnet=u)
    asignadasjson = serializers.serialize("json", asignacion)
    todasjson = serializers.serialize("json", todas)

    asig_lst = simplejson.loads(asignadasjson)
    todas_lst = simplejson.loads(todasjson)

    return simplejson.dumps({'todo': todas_lst, 'asignadas':asig_lst})

