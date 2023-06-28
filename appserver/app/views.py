from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

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