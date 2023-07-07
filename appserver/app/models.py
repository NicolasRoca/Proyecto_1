from distutils.command.upload import upload
from django.db import models

# Create your models here.
class producto(models.Model):
    descripcion=models.CharField(max_length=100)
    precio=models.IntegerField()
    tipo=models.CharField(max_length=20)
    imagen=models.ImageField(upload_to="productos", null=True)
    
    def _str_(self):
        return f'{self.descripcion} -> {self.precio}'
