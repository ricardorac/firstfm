import csv

# Dados reais
artistas = [
    {"ID": 1, "Nome": "The Beatles"},
    {"ID": 2, "Nome": "Michael Jackson"},
    {"ID": 3, "Nome": "Beyoncé"},
]

albuns = [
    {"ID": 1, "Nome": "Abbey Road", "Artista_ID": 1, "Genero": "Rock", "Ano_Lancamento": 1969},
    {"ID": 2, "Nome": "Revolver", "Artista_ID": 1, "Genero": "Rock", "Ano_Lancamento": 1966},
    {"ID": 3, "Nome": "Sgt. Pepper's Lonely Hearts Club Band", "Artista_ID": 1, "Genero": "Rock", "Ano_Lancamento": 1967},
    {"ID": 4, "Nome": "Thriller", "Artista_ID": 2, "Genero": "Pop", "Ano_Lancamento": 1982},
    {"ID": 5, "Nome": "Bad", "Artista_ID": 2, "Genero": "Pop", "Ano_Lancamento": 1987},
    {"ID": 6, "Nome": "Dangerous", "Artista_ID": 2, "Genero": "Pop", "Ano_Lancamento": 1991},
    {"ID": 7, "Nome": "Lemonade", "Artista_ID": 3, "Genero": "R&B", "Ano_Lancamento": 2016},
    {"ID": 8, "Nome": "Beyoncé", "Artista_ID": 3, "Genero": "Pop", "Ano_Lancamento": 2013},
    {"ID": 9, "Nome": "4", "Artista_ID": 3, "Genero": "Pop", "Ano_Lancamento": 2011},
]

musicas = [
    # Abbey Road
    {"ID": 1, "Nome": "Come Together", "Album_ID": 1, "Compositor": "John Lennon, Paul McCartney", "Duracao": "4:20"},
    {"ID": 2, "Nome": "Something", "Album_ID": 1, "Compositor": "George Harrison", "Duracao": "3:03"},
    {"ID": 3, "Nome": "Maxwell's Silver Hammer", "Album_ID": 1, "Compositor": "Paul McCartney", "Duracao": "3:27"},
    {"ID": 4, "Nome": "Oh! Darling", "Album_ID": 1, "Compositor": "Paul McCartney", "Duracao": "3:27"},
    {"ID": 5, "Nome": "Octopus's Garden", "Album_ID": 1, "Compositor": "Richard Starkey", "Duracao": "2:51"},
    # Revolver
    {"ID": 6, "Nome": "Taxman", "Album_ID": 2, "Compositor": "George Harrison", "Duracao": "2:39"},
    {"ID": 7, "Nome": "Eleanor Rigby", "Album_ID": 2, "Compositor": "Paul McCartney", "Duracao": "2:06"},
    {"ID": 8, "Nome": "I'm Only Sleeping", "Album_ID": 2, "Compositor": "John Lennon, Paul McCartney", "Duracao": "3:02"},
    {"ID": 9, "Nome": "Love You To", "Album_ID": 2, "Compositor": "George Harrison", "Duracao": "3:01"},
    {"ID": 10, "Nome": "Here, There and Everywhere", "Album_ID": 2, "Compositor": "Paul McCartney", "Duracao": "2:26"},
    # Sgt. Pepper's Lonely Hearts Club Band
    {"ID": 11, "Nome": "Sgt. Pepper's Lonely Hearts Club Band", "Album_ID": 3, "Compositor": "John Lennon, Paul McCartney", "Duracao": "2:02"},
    {"ID": 12, "Nome": "With a Little Help from My Friends", "Album_ID": 3, "Compositor": "John Lennon, Paul McCartney", "Duracao": "2:44"},
    {"ID": 13, "Nome": "Lucy in the Sky with Diamonds", "Album_ID": 3, "Compositor": "John Lennon, Paul McCartney", "Duracao": "3:28"},
    {"ID": 14, "Nome": "Getting Better", "Album_ID": 3, "Compositor": "John Lennon, Paul McCartney", "Duracao": "2:48"},
    {"ID": 15, "Nome": "Fixing a Hole", "Album_ID": 3, "Compositor": "John Lennon, Paul McCartney", "Duracao": "2:36"},
    # Thriller
    {"ID": 16, "Nome": "Wanna Be Startin' Somethin'", "Album_ID": 4, "Compositor": "Michael Jackson", "Duracao": "6:03"},
    {"ID": 17, "Nome": "Baby Be Mine", "Album_ID": 4, "Compositor": "Rod Temperton", "Duracao": "4:20"},
    {"ID": 18, "Nome": "The Girl Is Mine", "Album_ID": 4, "Compositor": "Michael Jackson", "Duracao": "3:42"},
    {"ID": 19, "Nome": "Thriller", "Album_ID": 4, "Compositor": "Rod Temperton", "Duracao": "5:58"},
    {"ID": 20, "Nome": "Beat It", "Album_ID": 4, "Compositor": "Michael Jackson", "Duracao": "4:18"},
    # Bad
    {"ID": 21, "Nome": "Bad", "Album_ID": 5, "Compositor": "Michael Jackson", "Duracao": "4:07"},
    {"ID": 22, "Nome": "The Way You Make Me Feel", "Album_ID": 5, "Compositor": "Michael Jackson", "Duracao": "4:58"},
    {"ID": 23, "Nome": "Speed Demon", "Album_ID": 5, "Compositor": "Michael Jackson", "Duracao": "4:01"},
    {"ID": 24, "Nome": "Liberian Girl", "Album_ID": 5, "Compositor": "Michael Jackson", "Duracao": "3:53"},
    {"ID": 25, "Nome": "Just Good Friends", "Album_ID": 5, "Compositor": "Terry Britten, Graham Lyle", "Duracao": "4:05"},
    # Dangerous
    {"ID": 26, "Nome": "Jam", "Album_ID": 6, "Compositor": "Michael Jackson, René Moore, Bruce Swedien, Teddy Riley", "Duracao": "5:39"},
    {"ID": 27, "Nome": "Why You Wanna Trip on Me", "Album_ID": 6, "Compositor": "Teddy Riley, Bernard Belle", "Duracao": "5:24"},
    {"ID": 28, "Nome": "In the Closet", "Album_ID": 6, "Compositor": "Michael Jackson, Teddy Riley", "Duracao": "6:31"},
    {"ID": 29, "Nome": "She Drives Me Wild", "Album_ID": 6, "Compositor": "Michael Jackson, Teddy Riley", "Duracao": "3:41"},
    {"ID": 30, "Nome": "Remember the Time", "Album_ID": 6, "Compositor": "Michael Jackson, Teddy Riley, Bernard Belle", "Duracao": "4:00"},
    # Lemonade
    {"ID": 31, "Nome": "Pray You Catch Me", "Album_ID": 7, "Compositor": "Beyoncé, Kevin Garrett, James Blake", "Duracao": "3:16"},
    {"ID": 32, "Nome": "Hold Up", "Album_ID": 7, "Compositor": "Beyoncé, Ezra Koenig, Emile Haynie, Thomas Wesley Pentz, Joshua Tillman, Sean Rhoden", "Duracao": "3:41"},
    {"ID": 33, "Nome": "Don't Hurt Yourself", "Album_ID": 7, "Compositor": "Beyoncé, Jack White, Diana 'Literature' Gordon", "Duracao": "3:54"},
    {"ID": 34, "Nome": "Sorry", "Album_ID": 7, "Compositor": "Beyoncé, Diana 'Literature' Gordon, Sean 'Melo-X' Rhoden, Hit-Boy, Stuart White", "Duracao": "3:53"},
    {"ID": 35, "Nome": "6 Inch", "Album_ID": 7, "Compositor": "Beyoncé, The Weeknd, Danny Schofield, Ben Billions, Boots", "Duracao": "4:20"},
    # Beyoncé
    {"ID": 36, "Nome": "Pretty Hurts", "Album_ID": 8, "Compositor": "Sia, Beyoncé", "Duracao": "4:17"},
    {"ID": 37, "Nome": "Haunted", "Album_ID": 8, "Compositor": "Beyoncé, Boots, Kelly Sheehan", "Duracao": "6:09"},
    {"ID": 38, "Nome": "Drunk in Love", "Album_ID": 8, "Compositor": "Beyoncé, Jay-Z, Detail, Timbaland", "Duracao": "5:23"},
    {"ID": 39, "Nome": "Blow", "Album_ID": 8, "Compositor": "Beyoncé, Pharrell Williams, Timbaland, Justin Timberlake", "Duracao": "5:09"},
    {"ID": 40, "Nome": "No Angel", "Album_ID": 8, "Compositor": "Caroline Polachek, Beyoncé, Boots", "Duracao": "3:49"},
    # 4
    {"ID": 41, "Nome": "1+1", "Album_ID": 9, "Compositor": "Beyoncé, The-Dream, Christopher Stewart", "Duracao": "4:35"},
    {"ID": 42, "Nome": "I Care", "Album_ID": 9, "Compositor": "Jeff Bhasker, Chad Hugo, Beyoncé", "Duracao": "3:59"},
    {"ID": 43, "Nome": "I Miss You", "Album_ID": 9, "Compositor": "Beyoncé, Frank Ocean, Shea Taylor", "Duracao": "2:59"},
    {"ID": 44, "Nome": "Best Thing I Never Had", "Album_ID": 9, "Compositor": "Babyface, Antonio Dixon, Patrick 'J. Que' Smith, Beyoncé", "Duracao": "4:13"},
    {"ID": 45, "Nome": "Party", "Album_ID": 9, "Compositor": "Kanye West, Jeff Bhasker, Beyoncé, André 3000", "Duracao": "4:05"},
]

# Função para criar e salvar CSV
def save_csv(filename, header, data):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

# Salvando arquivos CSV
save_csv("artistas.csv", ["ID", "Nome"], artistas)
save_csv("albuns.csv", ["ID", "Nome", "Artista_ID", "Genero", "Ano_Lancamento"], albuns)
save_csv("musicas.csv", ["ID", "Nome", "Album_ID", "Compositor", "Duracao"], musicas)

print("Arquivos CSV gerados com sucesso!")
