x = int(input("Inserire punto x: "))

y = int(input("Inserire punto y: "))

cordinate : tuple[int, int]= (x, y)

match cordinate:
    case 0, 0:
        print(f"Il punto {cordinate} si trova nell'origine.")
    case 0, y:
        print(f"Il punto {cordinate} si trova sull'asse delle x.")
    case x, 0:
        print(f"Il punto {cordinate} si trova sull'asse delle y.")
    case cordinate if x > 0 and y > 0:
        print(f"Il punto {cordinate} si trova nel primo quadrante.")
    case cordinate if x < 0 and y > 0:
        print(f"Il punto {cordinate} si trova nel secondo quadrante.")
    case cordinate if x < 0 and y < 0:
        print(f"Il punto {cordinate} si trova nel terzo quadrante.")
    case cordinate if x > 0 and y < 0:
        print(f"Il punto {cordinate} si trova nel quarto quadrante.")