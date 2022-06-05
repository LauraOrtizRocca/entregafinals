from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField(default=0.0)

class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)

class Alimento(models.Model):
    nombre_alimento = models.CharField(max_length=100)
    peso = models.FloatField(default=0.0)
    