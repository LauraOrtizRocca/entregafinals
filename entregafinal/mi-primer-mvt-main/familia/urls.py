from django.urls import path
from familia import views


urlpatterns = [
    path('', views.index, name="index"),
    path('agregar_persona/', views.agregar_persona, name="agregar_persona"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
    path('buscar/', views.buscar, name="buscar"),
    path('agregar_mascota/', views.agregar_mascota, name="agregar_mascota"),
]
