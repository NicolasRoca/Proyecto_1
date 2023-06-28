from math import prod
from tokenize import Pointfloat
from django.shortcuts import render
from .models import producto
from .forms import ProductoForm

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

def agregar_producto(request):
    data={
        'form': ProductoForm()
    }
    
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Guardado correctamente"
        else:
            data["form"]=formulario
    
    return render(request, 'app/producto/agregar.html', data)