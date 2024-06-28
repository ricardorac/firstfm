from django.contrib import admin
from .models import Album, Musica, Artista

admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Musica)
