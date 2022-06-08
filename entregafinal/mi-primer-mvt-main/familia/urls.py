from django.urls import path
from familia import views


urlpatterns = [
    path('index_2/', views.index_2, name="index_2"),
    path('', views.index, name="index"),
    path('agregar_persona/', views.agregar_pesona, name="agregar_persona"),
    path('borrar_persona/<identificador>', views.borrar_persona, name="borrar_persona"),
    path('buscar_persona/', views.buscar_persona, name="buscar_persona"),
    path('actualizar_persona/<identificador>', views.actualizar_persona, name="actualizar_persona"),
    path('agregar_mascota/', views.agregar_mascota, name="agregar_mascota"),
    path('borrar_mascota/<identificador>', views.borrar_mascota, name="borrar_mascota"),
    path('buscar_mascota/', views.buscar_mascota, name="buscar_mascota"),
    path('actualizar_mascota/<identificador>', views.actualizar_mascota, name="actualizar_mascota"),
]
