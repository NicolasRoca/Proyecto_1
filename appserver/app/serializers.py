from dataclasses import field
from urllib import request
from .models  import producto
from rest_framework import serializers  

class ProductoSerializer(serializers.ModelSerializer):
    descripcion=serializers.CharField(required=True, min_length=7)
    
    def validate_descripcion(self, value):
        existe =producto.objects.filter(descripcion__iexact=value).exists()
        
        if existe:
            raise serializers.ValidationError("Este producto ya existe")
        return value
    
    class Meta:
        model=producto
        fields='__all__'
