from django.db import models

# Create your models here.
class Artista(models.Model):
    nome = models.TextField()

class Album(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    genero = models.CharField(max_length=20, null=False)
    ano_lancamento = models.SmallIntegerField(null = True)

class Musica(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    compositor = models.TextField()
    duracao = models.CharField(max_length=5)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

class AvaliacaoMusica(models.Model):
    username = models.CharField(max_length=50, null=False)
    musica = models.ForeignKey(Musica, on_delete=models.CASCADE)
    nota = models.SmallIntegerField()
