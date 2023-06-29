from math import prod
from tokenize import Pointfloat
from django.shortcuts import render, redirect, get_object_or_404
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

def listar_productos(request):
    productos=producto.objects.all()
    
    data={
        'productos': productos
    }
    return render(request, 'app/producto/listar.html', data)

def modificar_producto(request, id):
    productos=get_object_or_404(producto, id=id)
    data={
        'form': ProductoForm(instance=productos)
    }
    
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"]=formulario
    
    return render(request, 'app/producto/modificar.html', data)