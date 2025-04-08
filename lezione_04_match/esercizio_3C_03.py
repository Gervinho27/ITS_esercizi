oggetti : list = []

for i in range(3):
    oggetto = input(f"Inserire l'oggetto {i + 1}: ")
    oggetti.append(oggetto)

match oggetti:
    case["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    case["sedia", "tavolo" , "armadio"]:
        print("Mobili")
    case["telefono", "computer", "tavolo"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")