from django.contrib import admin
from .models import producto
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display=["descripcion", "precio", "tipo"]
    list_editable=["precio"]
    search_fields=["tipo"]
    list_per_page: 6

admin.site.register(producto, ProductosAdmin)