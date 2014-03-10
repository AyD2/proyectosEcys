''' El siguiente modulo es el encargado de responder las peticiones.'''
from django.shortcuts import render
from sistema_pe import login as log
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def login(request):
    ''' Responde al request del index.
        En esta pagina se hace el login de usuario normal'''

    if request.method == 'POST':
        carnet = request.POST['usrCarnet']
        clave = request.POST['usrClave']
        if log.login(carnet, clave):
            request.session['carnet_usuario'] = carnet 
            request.session['logueado'] = True
            print "logeado satisfactoriamente"
            contexto = {'usuario': carnet, 'clave': clave
                , 'aceptado': False}
            return HttpResponseRedirect('/perfil')
        else:
            print "no se pudo logear"
            request.session['logueado'] = False
            contexto = {'usuario': nombre, 'clave': clave
                , 'aceptado': True}
            return render(request, 'proyectosEcys/index.html'
                , {'usuario':carnet 
                , 'clave': clave
                , 'aceptado': True})

def logout(request):
    del request.session['nombre_usuario']
    del request.session['logueado']
    return HttpResponseRedirect('/')

def index(request):
    contexto = {}
    return render(request, 'proyectosEcys/index.html', contexto)

def perfil(request):
    ''' responde al request de la pagina inicial de un usuario.
        La llamada se hace luego de un login satisfactorio'''
    #if hasattr(request.session, 'logueado'):
    return render(request, 'sistema_pe/usuario.html')
    #else:
    #    return HttpResponse("hijue cienmil putas que haces aqui mierda!!!!")
