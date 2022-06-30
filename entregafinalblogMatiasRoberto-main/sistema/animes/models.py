from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    episodios = models.IntegerField()
    estado = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion = models.TextField(max_length=500, verbose_name='Descripcion')
    autor = models.CharField(max_length=100)
    duracion = models.FloatField()

    def _str__(self):
        fila = "Titulo:" + self.titulo +  "-" + "Descripcion:" + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Serie(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    episodios = models.IntegerField()
    estado = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion = models.TextField(max_length=500, verbose_name='Descripcion')
    autor = models.CharField(max_length=100)
    duracion = models.FloatField()

    def _str__(self):
        fila = "Titulo:" + self.titulo +  "-" + "Descripcion:" + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen', null=True)
    descripcion = models.TextField(max_length=500, verbose_name='Descripcion')
    autor = models.CharField(max_length=100)
    duracion = models.FloatField()

    def _str__(self):
        fila = "Titulo:" + self.titulo +  "-" + "Descripcion:" + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Avatar(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatars", null=True, blank=True)
    nombre_usuario = models.CharField(max_length=100)

    def _str__(self):
        fila = "Titulo:" + self.titulo +  "-" + "Descripcion:" + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    
    def __str__(self):
        return self.titulo






