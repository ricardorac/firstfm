from .models import Album, Musica, Artista, AvaliacaoMusica

class CadastroAlbuns:

    def criar(titulo, artista_id, genero, ano_lancamento):
        a = Album()
        a.titulo = titulo
        a.artista = CadastroArtistas.obter(artista_id)
        a.genero = genero
        a.ano_lancamento = ano_lancamento
        a.save()
        return a
    
    def obter(id):
        return Album.objects.filter(id=id).first()
    
    def excluir(id):
        a = CadastroAlbuns.obter(id)
        a.delete()
    
    def atualizar(id, titulo, artista_id, genero, ano_lancamento):
        a = CadastroAlbuns.obter(id)
        if a is None:
            raise ValueError('Álbum não existe: id=', id)
        a.titulo = titulo
        a.artista = CadastroArtistas.obter(artista_id)
        a.genero = genero
        a.ano_lancamento = ano_lancamento
        a.save()
        return a
    
    def obter_ultimos_albuns(quantidade):
        return Album.objects.order_by("-id")[:quantidade]
    

class CadastroMusicas:

    def criar(titulo, compositor, duracao, album_id):
        m = Musica()
        m.titulo = titulo
        m.compositor = compositor
        m.duracao = duracao
        m.album = CadastroAlbuns.obter(album_id)
        m.save()
        return m
    
    def obter(id):
        return Musica.objects.filter(id=id).first()
    
    def excluir(id):
        m = CadastroMusicas.obter(id)
        m.delete()
    
    def atualizar(id, titulo, compositor, duracao, album_id):
        m = CadastroMusicas.obter(id)
        if m is None:
            raise ValueError('Música não existe: id=', id)
        m.titulo = titulo
        m.compositor = compositor
        m.duracao = duracao
        m.album = CadastroAlbuns.obter(album_id)
        m.save()
        return m
    
    def obter_ultimas_musicas(quantidade):
        return Musica.objects.order_by("-id")[:quantidade]

class CadastroArtistas:

    def criar(nome):
        a = Artista()
        a.nome = nome
        a.save()
        return a
    
    def obter(id):
        return Artista.objects.filter(id=id).first()
    
    def obter_por_nome(nome):
        return Artista.objects.filter(nome=nome).first()
    
    def excluir(id):
        a = CadastroArtistas.obter(id)
        a.delete()
    
    def atualizar(id, nome):
        a = CadastroArtistas.obter(id)
        if a is None:
            raise ValueError('Artista não existe: id=', id)
        a.nome = nome
        a.save()
        return a
    
    def obter_ultimos_artistas(quantidade):
        return Artista.objects.order_by("-id")[:quantidade]
    

class CadastroAvaliacoesMusica:

    def avaliar(username, musica_id, nota):
        musicas_avaliadas = CadastroAvaliacoesMusica.obter_avaliacoes_usuario(username)
        for avaliacao in musicas_avaliadas:
            if avaliacao.musica.id == musica_id:
                avaliacao.nota = nota
                avaliacao.save()
                return avaliacao
            
        ava = AvaliacaoMusica()
        ava.username = username
        ava.musica = CadastroMusicas.obter(musica_id)
        ava.nota = nota
        ava.save()
        return ava
    
    def obter(id):
        return AvaliacaoMusica.objects.filter(id=id).first()
    
    def obter_avaliacoes_usuario(username):
        return AvaliacaoMusica.objects.filter(username=username).all()