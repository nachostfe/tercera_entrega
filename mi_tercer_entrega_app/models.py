from django.db import models

from datetime import date
# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    duracion_semanas = models.IntegerField(default=4)
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Disco(models.Model):
    banda = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    fechaLanzamiento = models.DateField(default=date.today)
    precio=models.FloatField()

    def __str__(self):
        return f"{self.banda} {self.titulo}"
    
class Auto(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.marca} {self.modelo}'


class Recital(models.Model):
    banda = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    fecha = models.DateField()
    ciudad = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return f'{self.banda} {self.fecha}'
    
class Banda(models.Model):
    nombre = models.CharField(max_length=50)
    aniodeformacion = models.CharField(max_length=4)
    pais = models.CharField(max_length=50)
    historia = models.TextField(null=True, blank=True)
    genero = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre} {self.aniodeformacion}'