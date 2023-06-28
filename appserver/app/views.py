from math import prod
from django.shortcuts import render
from .models import producto

# Create your views here.

def home(request):
    Productos=producto.objects.all()
    data={
        'productos':Productos
    }
    return render(request, 'app/home.html', data)

def comprar(request):
    return render(request, 'app/comprar.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def camisetas(request):
    return render(request, 'app/camisetas.html')

def chuteadores(request):
    return render(request, 'app/chuteadores.html')

def guantes(request):
    return render(request, 'app/guantes.html')

def canilleras(request):
    return render(request, 'app/canilleras.html')