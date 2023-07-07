from dataclasses import dataclass
from math import prod
from tokenize import Pointfloat
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer
from .Carrito import Carrito

# Create your views here.

class ProductoViewset(viewsets.ModelViewSet):
    queryset=producto.objects.all()
    serializer_class=ProductoSerializer
    
    def get_queryset(self):
        productos=producto.objects.all()
        
        tipo=self.request.GET.get('tipo')
        
        if tipo:
            productos=productos.filter(tipo__contains=tipo)
        return productos
    

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

@permission_required('app.add_producto')
def agregar_producto(request):
    data={
        'form': ProductoForm()
    }
    
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado")
        else:
            data["form"]=formulario
    
    return render(request, 'app/producto/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(request):
    productos=producto.objects.all()
    
    page=request.GET.get('page',1)
    
    try:
        paginator=Paginator(productos, 5)
        productos=paginator.page(page)
    except:
        raise Http404
    
    data={
        'entity': productos,
        'paginator':paginator
    }
    return render(request, 'app/producto/listar.html', data)

@permission_required('app.change_producto')
def modificar_producto(request, id):
    productos=get_object_or_404(producto, id=id)
    data={
        'form': ProductoForm(instance=productos)
    }
    
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_productos")
        data["form"]=formulario
    
    return render(request, 'app/producto/modificar.html', data)


@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    productoeli=get_object_or_404(producto, id=id)
    productoeli.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_productos")

def registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    
    if request.method=='POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data['form']=formulario
    
    return render(request, 'registration/registro.html', data)

def tienda(request):
    productos=producto.objects.all()
    
    return render(request, "app/tienda.html", {'productos':productos})

def agregar_producto_carrito(request, producto_id):
    carrito=Carrito(request)
    Producto=producto.objects.get(id=producto_id)
    carrito.agregar(Producto)
    return redirect("tienda")

def eliminar_producto_carrito(request, producto_id):
    carrito=Carrito(request)
    Producto=producto.objects.get(id=producto_id)
    carrito.eliminar(Producto)
    return redirect("tienda")

def restar_producto_carrito(request, producto_id):
    carrito=Carrito(request)
    Producto=producto.objects.get(id=producto_id)
    carrito.restar(Producto)
    return redirect("tienda")


def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect("tienda")
