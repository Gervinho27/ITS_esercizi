def check_each(lista_numeri):
    for element in lista_numeri:
        if element > 5:
            print(f"{element} più grande di 5.")
        elif element < 5:
            print(f"{element} più piccolo di 5.")
        else:
            print(f"{element} ugule a 5.")
        