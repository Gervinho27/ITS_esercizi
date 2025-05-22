# importare dal modulo persona.py la classe Persona
from persona import Persona

class studente(Persona):

    '''
    Attributi della clsse persona
    self.name : str
    self.lastmane : str
    self.age : int

    Attributi della classe studente
    self.marticola : str

    '''

# inizializzare un oggetto della calsse studente
def __init__(self, name : str, lastname : str, age : int, matricola : str):

    # inizializzare la classe Persona richiamando il metodo init della superclasse. 
    super().__init__(name, lastname, age)

    #istruzioni che inizializzano un oggetto della classe Studente
    self.setmatricola(matricola)


# metodo setter

# metodo che importa il valore dell'attributo self.matricola
def setMatricola(self, matricola : str) -> None:
    if matricola:
        self.matricola = matricola
    else:
        print("Errore! La matricola non può essere rappresentata da una stringa vuota.")


# metodo getter

# metodo che ritorna il valore dell'attributo self matricola
def getMatricola(self) -> str:
    return self.matricola