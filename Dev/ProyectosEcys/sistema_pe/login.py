from hashlib import sha512
from sistema_pe.models import Usuario

def login(carnet, clave):
    try:
        us = Usuario.objects.get(carnet=carnet)
        if us.clave == sha512(clave).hexdigest():
            return True
        else:
            return False
    except:
        return False

def obtener_usuario(carnet):
    try:
        us = Usuario.objects.get(carnet=carnet)
        return us
    except:
        return None
