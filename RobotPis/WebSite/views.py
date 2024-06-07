from django.shortcuts import render, redirect
from Carrito.models import *
from .models import *
# Create your views here.

def materiales(request):
    return render(request, 'materiales.html')

def desarrolladores(request):
    return render(request, 'desarrolladores.html')

def vip(request):
    return render(request, 'vip.html')

def funcionamiento (request):
    return render(request, 'funcionamiento.html')

def testimonios(request):
    if request.method == 'POST':
        form = TestimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonios') 
    else:
        form = TestimonioForm()

    testimonios = Testimonio.objects.all().order_by('fecha')
    content = {
        'form': form, 
        'testimonios': testimonios
        }
    return render(request, 'testimonios.html', content)