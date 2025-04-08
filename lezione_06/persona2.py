class Persona:
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0

    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")
    
    # mi consente di impostare il nome di una persona
    def setname(self, name:str) -> None:
        self.name = name

    # mi consente di impostare il cognome di una persona
    def setlastname(self, lastname:str) -> None:
        self.lastname = lastname

    # mi consente di impostare l'età di una persona
    def setage(self, age:int) -> None:
        if age < 0 or age > 120:
            self.age = age
        else:
            self.age = age

    def getName(self) -> str:
        return self.name
    
    def getLastname(self) -> str:
        return self.lastname

    def getAge(self) -> int:
        return self.age
    

# creo un oggetto di tipo Persona
fm : Persona = Persona()

# imposto il nome di una persona
fm.setname("Luca")

# imposto il cognome di una persona
fm.setlastname("Marchetti")

# imposto l'età di una persona
fm.setage(20)

# mostro i dati di una persona
fm.displayData()

print("-------------------")
print(fm.getName(), fm.getLastname(), fm.getAge())