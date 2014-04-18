'''modulo encargado de manejar el login de un usuario'''
from hashlib import sha512
from sistema_pe.models import Usuario, Repositorio, Clase, Asignacion

def login(carnet, clave):
    '''funcion para hacer el login de usuario'''
    try:
        us = Usuario.objects.get(carnet=carnet)
        if us.clave == sha512(clave).hexdigest():
            return True
        else:
            return False
    except ValueError:
        return False

def obtener_usuario(carnet):
    '''funcion que trae un usuario especifico desde la base de datos'''
    try:
        us = Usuario.objects.get(carnet=carnet)
        return us
    except ValueError:
        return None


def obtener_repositorios(carnet):
    '''funcion que se encarga de buscar los repositorios de los proyectos
    de un usuario'''
    try:
        usu = Usuario.objects.get(carnet=carnet)
        rp = Repositorio.objects.filter(usuario=usu)
        return rp
    except ValueError:
        return None

def obtener_clases():
    '''funcion que se encarga de buscar todas las clases'''
    try:
        c = Clase.objects.all()
        return c
    except ValueError:
        return None

def obtener_usuario(carnet):
    '''trae el objeto usuario'''
    try:
        u = Usuario.objects.get(carnet=carnet)
        return u
    except ValueError:
        return None

def obtener_mis_clases(carnet):
    '''trae el objeto usuario'''
    try:
        u = Usuario.objects.get(carnet=carnet)
        asignadas = Asignacion.objects.filter(id_carnet=u)
        #revisar las que esten activas nada mas!!!!!!!!!!!!!
        return asignadas
    except ValueError:
        return None
