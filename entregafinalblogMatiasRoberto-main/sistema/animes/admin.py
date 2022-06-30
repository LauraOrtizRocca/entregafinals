from django.contrib import admin
from animes.models import Anime, Serie, Pelicula, Avatar

# Register your models here.

admin.site.register(Anime)
admin.site.register(Serie)
admin.site.register(Pelicula)
admin.site.register(Avatar)