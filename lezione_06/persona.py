class Persona:
    '''
    Di questa persona dobbiamo sapere delle informazioni.
    Queste informazioni vengono chiamate attributi (delle classi Persona)
    Le informazioni saranno:
    - nome
    - cognome
    - età
    
    come li rappresento in Python?

    self.name:str (attributo di tipo stringa)
    self.lastname:str (attributo di tipo stringa)
    self.age:int (attributo di tipo intero)
    '''

    # costruttore della classe Persona
    def __init__(self, name:str, lastname:str, age:int):
        self.name = name
        self.lastname = lastname
        self.age = age

    # funzione che mostri in output tutte informazioni della persona
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")



fm = Persona("Luca", "Marchetti", 20)

print(fm)

# mostra i dati diuna persona
fm.displayData()