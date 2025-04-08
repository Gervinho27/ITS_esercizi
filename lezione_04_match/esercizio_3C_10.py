giorni = int(input("Inserire il giorno: "))
mesi = int(input("Inserire il mese: "))

data : tuple[int, int] = (giorni, mesi)

giorni_per_mese : list[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

match data:
    case (1, 1):
        print(f"Il giorno {giorni} / {mesi} è Capodanno!")
    case (14, 2):
        print(f"Il giorno {giorni} / {mesi} è San Valentino!")
    case (2, 6):
        print(f"Il giorno {giorni} / {mesi} è Festa della Repubblica Italiana!")
    case (15, 8):
        print(f"Il giorno {giorni} / {mesi} è Ferragosto!")
    case (31, 9):
        print(f"Il giorno {giorni} / {mesi} è Halloween!")
    case (25, 12):
        print(f"Il giorno {giorni} / {mesi} è Natale!")
    case (giorni, mesi) if mesi > 12 or giorni > giorni_per_mese[mesi - 1]:
        print(f"Il {giorni} / {mesi} non esiste!")
    case (_):
        print(f"Nessuna festività importante in questa data.")