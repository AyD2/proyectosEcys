from django.shortcuts import render

#Create your views here.

def index(request):
    context = 1
    return render(request,'login/index.html',context)
