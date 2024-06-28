from django.shortcuts import render
from django.views import View
from .cadastros import CadastroAlbuns, CadastroArtistas, CadastroMusicas, CadastroAvaliacoesMusica

# Create your views here.

class HomeView(View):
    def get(self, request):
        ultimos_artistas = CadastroArtistas.obter_ultimos_artistas(10)
        ultimos_albuns = CadastroAlbuns.obter_ultimos_albuns(10)
        ultimas_musicas = CadastroMusicas.obter_ultimas_musicas(50)
        context = {'albuns' : ultimos_albuns, 'artistas' : ultimos_artistas, 'musicas' : ultimas_musicas}
        return render(request, 'index.html', context)
    
class AlbunsView(View):
    def get(self, request):
        ultimos_albuns = CadastroAlbuns.obter_ultimos_albuns(10)
        context = {'albuns' : ultimos_albuns}
        return render(request, 'index.html', context)
    
class AlbumView(View):
    def get(self, request, id):
        album = CadastroAlbuns.obter(id)
        context = {'album' : album}
        return render(request, 'album.html', context)
    
    
class AvaliacaoMusicaView(View):
    def get(self, request, musica_id, nota):
        if request.user.is_authenticated:
            username = request.user.username
        else:
            username = 'anonymous'
        CadastroAvaliacoesMusica.avaliar(username, musica_id, nota)
        context = {}
        return render(request, 'album.html', context)