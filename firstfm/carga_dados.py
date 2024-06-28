from firstapp.cadastros import CadastroAlbuns, CadastroArtistas, CadastroMusicas

import csv

# Função para carregar dados do CSV
def load_csv(filename):
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def executa():
    # Carregando dados dos arquivos CSV
    artistas = load_csv("artistas.csv")
    albuns = load_csv("albuns.csv")
    musicas = load_csv("musicas.csv")

    # Exibindo os dados carregados
    print("Artistas:")
    for artista in artistas:
        CadastroArtistas.criar(artista['Nome'])

    print("\nÁlbuns:")
    for album in albuns:
        CadastroAlbuns.criar(album['Nome'], album['Artista_ID'], album['Genero'], album['Ano_Lancamento'])

    print("\nMúsicas:")
    for musica in musicas:
        CadastroMusicas.criar(musica['Nome'], musica['Compositor'], musica['Duracao'], musica['Album_ID'])
