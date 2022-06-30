from django import forms
from .models import Anime, Serie, Pelicula, Avatar



class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'

class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'




"""class AnimeForm(forms.Form):
    id = forms.AutoField(primary_key=True)
    titulo = forms.CharField(max_length=100, verbose_name='Titulo')
    episodios = forms.IntegerField()
    estado = forms.CharField(max_length=100)
    imagen = forms.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion = forms.TextField(max_length=500, verbose_name='Descripcion')
    autor = forms.CharField(max_length=100)
    duracion = forms.FloatField(0.0)

class SerieForm(forms.Form):
    id = forms.AutoField(primary_key=True)
    titulo = forms.CharField(max_length=100, verbose_name='Titulo')
    episodios = forms.IntegerField()
    estado = forms.CharField(max_length=100)
    imagen = forms.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion = forms.TextField(max_length=500, verbose_name='Descripcion')
    autor = forms.CharField(max_length=100)
    duracion = forms.FloatField(0.0)

class PeliculaForm(forms.Form):
    id = forms.AutoField(primary_key=True)
    titulo = forms.CharField(max_length=100, verbose_name='Titulo')
    imagen = forms.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion = forms.TextField(max_length=500, verbose_name='Descripcion')
    autor = forms.CharField(max_length=100)
    duracion = forms.FloatField(0.0)"""