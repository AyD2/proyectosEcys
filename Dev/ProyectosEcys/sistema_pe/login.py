'''modulo encargado de manejar el login de un usuario'''
from hashlib import sha512
from sistema_pe.models import Usuario, Repositorio

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
    '''funcion que se encarga de buscar los enunciados de los proyectos
    de un usuario'''
    try:
        usu = Usuario.objects.get(carnet=carnet)
        rp = Repositorio.objects.filter(usuario=usu)
        return rp
    except ValueError:
        return None
