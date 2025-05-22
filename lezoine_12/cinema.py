class MovieCatalog:

    '''
    Attributi della classe Movie Catalog
    self.Catalog: dict[str, list[str]]

    '''

    # Inizializzare un oggetto della classe MovieCatalog
    def __init__(self) -> None :
        self.setCatalog()

    # Metodi setter

    # Metodo che imposta il valore dell'attributo self.Catalog
    def setCatalog(self) -> None :
        self.catalog: dict[str, list[str]] = {}

    # metodo getter

    # Metodo che ristorna il valore dell'attributo self.catalog
    def getCatalog(self) -> dict[str, list[str]]:
        return self.catalog
    
    #Metodi della classe MovieCatalog

    #metodo che aggiunge una lista di film al catalogo
    def add(self, director_name: str, movies: list[str]) -> None:
        #check valore valido di director_name
        if not director_name:
            print("Fornire un nome valido per regista")
        #check valore valido di movies
        elif not movies:
            print("Fornire una lista di film che non sia vuota")
        #se i dati inseriti sono validi
        else:
            
            #se il regista è presente nel catalogo, aggiungi i film
            if director_name in self.catalog:
                #aggiungere film nel catalogo
                for movie in movies:
                    #controlliamo se i film della lista movies sono già stati inseriti dentro al catalogo
                    #dizionario[key] -> ritorna il vlore corrispondente alla chiave key
                    #self.catalog[director_name] è la lista dei film prodotti dal regista directo_name
                    #dove self.catalog è un dizionario
                    #director_name è la chiave
                    #self.catalog[director_name] è il valore corrispondente ala chiave director_name
                    if movie in self.catalog[director_name]:
                        print(f"Il film {movie} è già presente nel catalogo")

                    #un film della lista movies non è già presente nel catalogo
                    else:
                        #aggiungiamo il film al catalogo
                        self.catalog[director_name].append(movie)