from django.urls import path
from .views import home, comprar, carrito, camisetas, chuteadores, guantes

urlpatterns=[
    path('', home, name="home"),
    path('comprar/', comprar, name="comprar"),
    path('carrito/', carrito, name="carrito"),
    path('camisetas/', camisetas, name="camisetas"),
    path('chuteadores/', chuteadores, name="chuteadores"),
    path('guantes/', guantes, name="guantes"),
]