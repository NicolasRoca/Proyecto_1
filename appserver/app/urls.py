from django.urls import path
from .views import home, comprar, carrito, camisetas, chuteadores, guantes, canilleras, agregar_producto

urlpatterns=[
    path('', home, name="home"),
    path('comprar/', comprar, name="comprar"),
    path('carrito/', carrito, name="carrito"),
    path('camisetas/', camisetas, name="camisetas"),
    path('chuteadores/', chuteadores, name="chuteadores"),
    path('guantes/', guantes, name="guantes"),
    path('canilleras/', canilleras, name="canilleras"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
]