from django.shortcuts import redirect, render
from django.http import HttpResponse
from animes.models import Anime, Avatar, Serie, Pelicula
from .forms import AnimeForm, SerieForm, PeliculaForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


# Create your views here.

        #CREO ANIME Y TODAS SUS COSAS

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

        #DEFINO ANIMES Y TODAS SUS COSAS

def animes(request):
    animes = Anime.objects.all()
    return render(request, 'animes/index.html', {'animes': animes})
@login_required
def crear_anime(request):
    formulario = AnimeForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('animes')
    return render(request, 'animes/crear_anime.html', {'formulario': formulario})

@login_required
def actualizar_anime(request, id):
    anime = Anime.objects.get(id=id)
    formulario = AnimeForm(request.POST or None, request.FILES or None, instance=anime)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('animes')
    return render(request, 'animes/actualizar_anime.html', {'formulario': formulario})

@login_required
def borrar_anime(request, id):
    anime = Anime.objects.get(id=id)
    anime.delete()
    return redirect('animes')

        #CREO SERIES Y TODAS SUS COSAS

def series(request):
    series = Serie.objects.all()
    return render(request, 'series/index.html', {'series': series})

@login_required
def crear_serie(request):
    formulario = SerieForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('series')
    return render(request, 'series/crear_serie.html', {'formulario': formulario})

@login_required
def actualizar_serie(request, id):
    serie = Serie.objects.get(id=id)
    formulario = SerieForm(request.POST or None, request.FILES or None, instance=serie)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('series')
    return render(request, 'series/actualizar_serie.html', {'formulario': formulario})

@login_required
def borrar_serie(request, id):
    serie = Serie.objects.get(id=id)
    serie.delete()
    return redirect('series')

        # CREO PELICULAS Y TODAS SUS COSAS

def peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/index.html', {'peliculas': peliculas})

@login_required
def crear_pelicula(request):
    formulario = PeliculaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('peliculas')
    return render(request, 'peliculas/crear_pelicula.html', {'formulario': formulario})

@login_required
def actualizar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    formulario = PeliculaForm(request.POST or None, request.FILES or None, instance=pelicula)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('peliculas')
    return render(request, 'peliculas/actualizar_pelicula.html', {'formulario': formulario})

@login_required
def borrar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return render(request, 'peliculas')

         # CREO LA VISTA FAVORITOS

def favoritos(request):
    return render(request, 'paginas/favoritos.html', {})


         # CREO TODA LA FASE DEL USUARIO

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'usuarios/usuario_crear_cuenta_form.html'
  success_url = reverse_lazy('usuario_login')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

class BloggerProfile(DetailView):

    model = User
    template_name = "usuarios/usuario_detail.html"


class BloggerUpdate(LoginRequiredMixin, UpdateView):

    model = User
    template_name = "usuarios/usuario_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
      return reverse_lazy("usuario_profile", kwargs={"pk": self.request.user.id})

class UsuarioLogin(LoginView):
    template_name = 'usuarios/usuario_login.html'
    next_page = reverse_lazy("nosotros")


class UsuarioLogout(LogoutView):
    template_name = 'usuarios/usuario_logout.html'

class UsuarioList(ListView):

    model = Avatar
    template_name = "usuarios/usuario_list.html"
