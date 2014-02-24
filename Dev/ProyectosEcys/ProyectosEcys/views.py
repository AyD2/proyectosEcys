from django.shortcuts import render
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('proyectosEcys/index.html', c)
