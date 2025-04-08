class Persona:

    def __init__(self, nome, cognome, eta):
        
        self.__nome = nome
        self.cognome = cognome
        self.eta = eta

    def get_nome(self):
        return self.nome
    


persona_1 : Persona = Persona("Mario", "Rossi", "30")
persona_2 : Persona = Persona("Flavio", "Giorgi", "31")
persona_3 : Persona = Persona("Paolo", "Bianchi", "23")
persona_4 : Persona = Persona("Paolo", "Bianchi", "23")

persona_1.__nome
persona_2.__nome
persona_3.__nome
persona_4.__nome


pass