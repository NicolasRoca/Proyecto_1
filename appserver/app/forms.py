import imp
from pyexpat import model
from django import forms
from .models import producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class ProductoForm(forms.ModelForm):
    
    descripcion=forms.CharField(min_length=10, max_length=50)
    precio=forms.IntegerField(min_value=5000, max_value=150000)
    tipo=forms.CharField(min_length=7, max_length=12)
    imagen=forms.ImageField(validators=[MaxSizeFileValidator(max_file_size=2)])
    
    def clean_descripcion(self):
        descripcion=self.cleaned_data["descripcion"]
        existe=producto.objects.filter(descripcion__iexact=descripcion).exists()
        
        if existe:
            raise ValidationError("Este produto ya existe")
        return descripcion
    
    class Meta:
        model=producto
        fields='__all__'
        
class CustomUserCreationForm(UserCreationForm):
    
    
    
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']