from dataclasses import field
from .models  import producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=producto
        fields='__all__'
