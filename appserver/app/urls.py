from django.urls import path
from .views import home, comprar, carrito, camisetas, chuteadores 
from .views import guantes, canilleras, agregar_producto
from .views import listar_productos, modificar_producto, eliminar_producto

urlpatterns=[
    path('', home, name="home"),
    path('comprar/', comprar, name="comprar"),
    path('carrito/', carrito, name="carrito"),
    path('camisetas/', camisetas, name="camisetas"),
    path('chuteadores/', chuteadores, name="chuteadores"),
    path('guantes/', guantes, name="guantes"),
    path('canilleras/', canilleras, name="canilleras"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
]