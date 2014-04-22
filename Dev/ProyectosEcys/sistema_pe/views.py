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
        try:
            tutor = request.POST['tutor']
        except:
            tutor = False
        if tutor:
            if log.login_tutor(carnet, clave):
                request.session['carnet_usuario'] = carnet
                request.session['logueado'] = True
                print "logeado satisfactoriamente"
                return HttpResponseRedirect('/tutor')
            else:
                print "no se pudo logear"
                request.session['logueado'] = False
                return render(request, 'proyectosEcys/index.html'
                    , {'usuario':carnet
                    , 'clave': clave
                    , 'aceptado': True})
        else:
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



def upload(request):
    response_data = {}

    if request.is_ajax():
        form = UploaderForm(request.POST, request.FILES)

    if form.is_valid():
        proyecto = Proyecto(
            clase = Clase.objects.get(),
            creador = Usuario.objects.get(),
            fecha_entrega = request.
            upload=request.FILES['upload'],
        )
        upload.name = request.FILES['upload'].name
        upload.save()

        response_data['status'] = "success"
        response_data['result'] = "Your file has been uploaded:"
        response_data['fileLink'] = "/%s" % upload.upload

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    response_data['status'] = "error"
    response_data['result'] = "We're sorry, but something went wrong. Please be sure that your file respects the upload conditions."

    return HttpResponse(json.dumps(response_data), content_type='application/json')


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

def tutor(request):
    ''' responde al request de la pagina inicial de un usuario.
        La llamada se hace luego de un login satisfactorio'''
#poner los proyectos!!!!!!!!!!!!!!!!!!!!
    carnet = request.session['carnet_usuario']
    usuario = log.obtener_usuario(carnet)
    return render(request, 'sistema_pe/tutor.html',
            {'carnet':request.session['carnet_usuario']})


