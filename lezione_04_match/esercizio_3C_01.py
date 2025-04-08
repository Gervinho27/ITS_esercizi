voto = int(input("Inserisci voto: "))
match voto:
    case 10:
        print("Eccellente!")
    case 8 | 9:
        print("Molto buono")
    case 6 | 7:
        print("Sufficente")
    case  4 | 5:
        print("Insufficente")
    case 1 | 3:
        print("Gravemente insufficente!")
    case _ :
        print("Voto non valido!") 