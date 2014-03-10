from django.shortcuts import render
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def home(request):
    c = {}
    c.update(csrf(request))
    return HttpResponseRedirect('/usuario/', c)
