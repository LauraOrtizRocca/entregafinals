from django.urls import path
from Blog import views

urlpatterns = [
    path("", views.BlogList.as_view(), name="blog_list"),
    path("Crear/", views.BlogCreate.as_view(), name="blog_create"),
    path("Detalles/<pk>/", views.BlogDetail.as_view(), name ="blog_detail"),
    path("Editar/<pk>/", views.BlogUpdate.as_view(), name ="blog_update"),
    path("Borrar/<pk>/", views.BlogDelete.as_view(), name ="blog_delete"),
    path("Ingresar/", views.BlogLogin.as_view(), name="blog_login"),
    path("Salir/", views.BlogLogout.as_view(), name="blog_logout"),
]