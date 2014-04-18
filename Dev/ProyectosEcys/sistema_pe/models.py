from django.db import models

# Create your models here.

class Usuario(models.Model):
    carnet = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=10)
    clave = models.CharField(max_length=128)
    tipo_usuario = models.BooleanField()
    correo = models.CharField(max_length=50)

class Asignacion(models.Model):
    id_carnet = models.ForeignKey('Usuario')
    id_Clase = models.ForeignKey('Clase')


class Repositorio(models.Model):
    proyecto = models.ForeignKey('Proyecto')
    usuario = models.ForeignKey('Usuario')
    direccion = models.CharField(max_length=50)

class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=2)
    semestre = models.ForeignKey('Semestre')
    tutor = models.ForeignKey('Usuario')
    #activa = models.BooleanField()

class Semestre(models.Model):
    year = models.IntegerField()
    etapa = models.IntegerField()

class Proyecto(models.Model):
    clase = models.ForeignKey('Clase')
    creador = models.ForeignKey('Usuario')
    fecha_entrega = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now=True)
    contenido = models.CharField(max_length=50)
    #activo = models.BooleanField()
