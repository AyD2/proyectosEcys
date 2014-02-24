from django.shortcuts import render
from hashlib import sha512
from sistema_pe import login as log

# Create your views here.

def index(request):
    if request.method == 'POST':
        nombre = request.POST['usrNombre']
        clave = request.POST['usrClave']
        if log.login(nombre, clave):
            print "logeado satisfactoriamente"
            contexto = {'usuario': nombre, 'clave': clave, 'aceptado': False}
            return render(request, 'sistema_pe/index.html', contexto)
        else: 
            print "no se pudo logear"
            contexto = {'usuario': nombre, 'clave': clave, 'aceptado': True}
            return render(request, 'proyectosEcys/index.html', {'usuario': nombre, 'clave': clave, 'aceptado': True})


def login(request):
    if request.method == 'POST':
        print "formularioo!!!"
