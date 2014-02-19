from hashlib import sha512
from sistema_pe.models import Usuario

def login(nombre, clave):
    try:
        us = Usuario.objects.get(nombre=nombre)
        if us.clave == sha512(clave).hexdigest():
            return False
        else:
            return False
    except:
        return False
    
def obtener_usuario(nombre):
    try:
        us = Usuario.objects.get(nombre=nombre)
        return us
    except:
        return None
