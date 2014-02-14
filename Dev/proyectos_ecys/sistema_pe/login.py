from hashlib import sha512
from sistema_pe.models import Usuario

def login(nombre, clave):
    print nombre
    print clave

def obtener_usuario(nombre):
    try:
        us = Usuario.objects.get(nombre=nombre)
        return us
    except:
        return None
