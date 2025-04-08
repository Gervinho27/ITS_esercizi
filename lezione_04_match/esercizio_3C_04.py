mammiferi : list = ["cane", "gatto", "cavallo", "elefante", "leone"]
rettili : list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli : list = ["aquila", "pappagallo", "gufo", "falco"]
pesci : list = ["squalo", "trota", "salmone", "carpa"]

animale = input("Inserire l'animale: ")
match animale:
    case animale if animale in mammiferi:
        print(f"{animale} appartiene alla categoria dei mammiferi!")
    case animale if animale in rettili:
        print(f"{animale} appartiene alla categoria dei rettili!")
    case animale if animale in uccelli:
        print(f"{animale} appartiene alla categoria degli uccelli!")
    case animale if animale in pesci:
        print(f"{animale} appartiene alla categoria dei pesci!")
    case _ :
        print(f"Non so dire in quale categoria appartiene l'animale {animale}!")