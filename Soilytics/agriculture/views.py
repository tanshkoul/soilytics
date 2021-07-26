from django.shortcuts import render
from django.http import HttpResponse
from .forms import AmbeeForm

# Create your views here.

def index(request):
    return render(request, 'agriculture/index.html')

def landing(request):
    return render(request, 'agriculture/landing.html')

def soildata(request):
    result = {}
    if 'city' and 'country' in request.GET:
        form = AmbeeForm(request.GET)
        if form.is_valid():
            result = form.gather()
    
    else:
        form = AmbeeForm()

    return render(request, 'agriculture/soildata.html', {'form': form, 'result': result})

def plantdata(request):
    return render(request, 'agriculture/plantasium.html')