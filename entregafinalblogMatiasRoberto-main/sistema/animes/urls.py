from xml.dom.minidom import Document
from django.urls import path
from animes import views

from django.conf import Settings, settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('animes/', views.animes, name='animes'),
    path('animes/crear_anime', views.crear_anime, name='crear_anime'),
    path('animes/actualizar_anime', views.actualizar_anime, name='actualizar_anime'),
    path('borrar_anime/<int:id>', views.borrar_anime, name='borrar_anime'),
    path('animes/actualizar_anime/<int:id>', views.actualizar_anime, name='actualizar_anime'),
    path('series', views.series, name='series'),
    path('series/crear_serie', views.crear_serie, name='crear_serie'),
    path('series/actualizar_serie', views.actualizar_serie, name='actualizar_serie'),
    path('borrar_serie/<int:id>', views.borrar_serie, name='borrar_serie'),
    path('series/actualizar_serie/<int:id>', views.actualizar_serie, name='actualizar_serie'),
    path('peliculas', views.peliculas, name='peliculas'),
    path('peliculas/crear_pelicula', views.crear_pelicula, name='crear_pelicula'),
    path('peliculas/actualizar_pelicula', views.actualizar_pelicula, name='actualizar_pelicula'),
    path('borrar_pelicula/<int:id>', views.borrar_pelicula, name='borrar_pelicula'),
    path('peliculas/actualizar_pelicula/<int:id>', views.actualizar_pelicula, name='actualizar_pelicula'),
    path('paginas/favoritos', views.favoritos, name='favoritos'),
    path("usuarios/crear_usuario/", views.SignUpView.as_view(), name ="usuario_signup"),
    path("usuarios/perfil_usuario/<pk>/", views.BloggerProfile.as_view(), name ="usuario_profile"),
    path("usuarios/editar_usuario/<pk>/", views.BloggerUpdate.as_view(), name ="usuario_edit"),
    path("usuarios/entrar/", views.UsuarioLogin.as_view(), name="usuario_login"),
    path("usuarios/salir/", views.UsuarioLogout.as_view(), name="usuario_logout"),
    path("usuarios/lista_usuarios", views.UsuarioList.as_view(), name="usuario_list"),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
