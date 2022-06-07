from django.urls import path
from familia import views


urlpatterns = [
    path('', views.index, name="index"),
    path('agregar_persona/', views.agregar_pesona, name="agregar_persona"),
    path('borrar_persona/<identificador>', views.borrar_persona, name="borrar_persona"),
    path('buscar_persona/', views.buscar_persona, name="buscar_persona"),
    path('actualizar_persona/<identificador>', views.actualizar_persona, name="actualizar_persona"),
]
