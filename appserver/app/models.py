from django.db import models

# Create your models here.
class producto(models.Model):
    descripcion=models.CharField(max_length=100)
    precio=models.IntegerField()
    tipo=models.CharField(max_length=20)
    
    def _str_(self):
        return self.descripcion
