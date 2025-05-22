#dal modulo cinema.py importare le classe MovieCatalog
from cinema import MovieCatalog

# creare un oggetto della MovieCatalog
catalog: MovieCatalog = MovieCatalog()

#aggiungiamo un regista e dei film al catalogo
catalog.add_movie('Steven Spielberg', ['Casper', 'Ritorno al futuro'])

catalog.add_movie('Steven Spielberg', ['ET'])

catalog.addmovie('Quentin Tarantino', ['Pulp Fiction', 'Kill Bill'])

catalog.remove_movie('Steven Spielberg', 'ET')
catalog.remove_movie('Steven Spielberg', 'Ritorno al futuro')
catalog.remove_movie('Steven Spielberg', 'Casper')

print(catalog.getcatalog())