'''modulo encargado de manejar el login de un usuario'''
from hashlib import sha512
from sistema_pe.models import Usuario

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
