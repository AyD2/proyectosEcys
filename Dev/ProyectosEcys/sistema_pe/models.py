from django.db import models

# Create your models here.

class Usuario(models.Model):
        nombre = models.CharField(max_length=10)
        clave = models.CharField(max_length=128)

