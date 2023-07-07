from django.urls import path, include
from .views import home, comprar, carrito, camisetas, chuteadores, \
                    guantes, canilleras, agregar_producto, \
                    listar_productos, modificar_producto, \
                    eliminar_producto, registro, ProductoViewset, tienda, \
                    agregar_producto_carrito, eliminar_producto_carrito, \
                    restar_producto_carrito, limpiar_carrito
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register('producto', ProductoViewset)

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
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('carrito/', views.carrito, name='carrito'),
    path('tienda/', tienda, name='tienda'),  
    path('agregar_producto_carrito/<int:producto_id>/', agregar_producto_carrito, name='agregar_producto_carrito'), 
    path('eliminar_producto_carrito/<int:producto_id>/', eliminar_producto_carrito, name='eliminar_producto_carrito'), 
    path('restar_producto_carrito/<int:producto_id>/', restar_producto_carrito, name='restar_producto_carrito'), 
    path('limpiar_carrito/', limpiar_carrito, name='limpiar_carrito'), 
]