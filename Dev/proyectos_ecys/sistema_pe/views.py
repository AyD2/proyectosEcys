from django.shortcuts import render

# Create your views here.

def index(request):
    print "mierda"
    return render(request, 'sistema_pe/index.html')

def login(request):
    if request.method == 'POST':
        print "formularioo!!!"
