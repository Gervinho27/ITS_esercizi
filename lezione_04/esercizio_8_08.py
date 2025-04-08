def make_album(artista, album, num_canzoni=None):
    album={'artista': artista, 'album' : album}
    if num_canzoni:
        album['num_canzoni'] = num_canzoni
    return album

while True:
    artista = str(input("Inserisci il nome dell'artista: "))
    if artista == "quit": 
        break    
    album = str(input("Inserisci nome dell'album: "))
    print(make_album(artista, album))