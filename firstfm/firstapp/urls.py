from django.urls import path

from . import views

app_name = 'firstapp'
urlpatterns = [
    # ex: /firstfm/
    path("", views.HomeView.as_view(), name="index"),
    # ex: /forum/5/
    path("album/<int:id>/", views.AlbumView.as_view(), name="album_detail"),
    # ex: /forum/5/vote/
    path("avaliar/<int:musica_id>/<int:nota>/", views.AvaliacaoMusicaView.as_view(), name="avaliar_musica"),
]