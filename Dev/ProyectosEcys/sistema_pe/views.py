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
            return HttpResponseRedirect('/perfil')
        else:
            print "no se pudo logear"
            request.session['logueado'] = False
            return render(request, 'proyectosEcys/index.html'
                , {'usuario':carnet
                , 'clave': clave
                , 'aceptado': True})


def logout(request):
    '''salir'''
    del request.session['nombre_usuario']
    del request.session['logueado']
    return HttpResponseRedirect('/')


def index(request):
    '''respuesta cuando se pide al servidor el index'''
    contexto = {}
    return render(request, 'proyectosEcys/index.html', contexto)


def perfil(request):
    ''' responde al request de la pagina inicial de un usuario.
        La llamada se hace luego de un login satisfactorio'''
    carnet = request.session['carnet_usuario']
    repos = log.obtener_repositorios(carnet)
    clases = log.obtener_clases()
    usuario = log.obtener_usuario(carnet)
    misclases = log.obtener_mis_clases(carnet)
    return render(request, 'sistema_pe/usuario.html',
            {'carnet':request.session['carnet_usuario'], 'repos':repos,
                'clases':clases,'misclases':misclases, 'usuario':usuario})




