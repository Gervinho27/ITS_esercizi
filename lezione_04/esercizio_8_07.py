def make_album(artista, titolo, num_canzoni=None):
    album={'artista': artista, 'titolo' : titolo}
    if num_canzoni:
        album['num_canzoni'] = num_canzoni
    return album
album1 = make_album('Carattere speciale', 'Tha Supreme')
album2 = make_album('Utopia', 'Travis Scott')
album3 = make_album('Burattino senza fili', 'Edoardo Bennato')

print(album1)
print(album2)
print(album3)

album4 = make_album('Esci dal tunnel', 'Simba la rue', 26)
print(album4)