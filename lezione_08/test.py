from persona import Persona
from studente import Studente

# creo una lista della calsse Persona
fm : Persona = Persona("Luca", "Marchetti", 20)

# visualizzare le informazioni relative all'oggetto fm
print(fm)

# creo un oggetto della classe Studente
studente1 : Studente = Studente("Mario", "Rossi", 30, "0123456")

# visualizzare le informazioni relative all'oggetto studente1
print(studente1)

# controlo se studente1 sia istanza sella classe Studente
# isinstance(obj, Class)->  controlla se l'oggetto sia istanza della calsse studente1
# in caso affermativo -> True
# in caso negativo -> False
if isinstance(studente1, Studente):
    print("\nstudente1 è istanza della classe Studente")

# controllo se studente1 è istanza della classe studente1
if isinstance(studente1, Persona):
    print("\nstudente1 è anche istanza della calsse Persona")

# controllare se l'oggetto fm sia istaza della classe Persona
if isinstance(fm, Persona):
    print("\nl'oggetto fm è istanza della classe Persona")

# controllare se l'oggetto fm sia anche istanza della classe Studente
if isinstance(fm, Studente):
    print("/nl'oggetto fm è istanza della calsse Persona ed è anche istanza della classe Studente")
else:
    print("\nl'oggetto fm è istanza della calsse Persona ma non è istanza della classe Studente")

# controllare che la calsse Studente sia sottoclasse della classe Persona
# issubclass(Class1, Class2) -> controlla se Class1 sia sottoclasse della clsse Class2
# in caso affermativo -> True
# in caso negativo -> False
if issubclass(Studente, Persona):
    print("\nla calsse Studente è sottoclasse dela classe Persona")