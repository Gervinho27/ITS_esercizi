def check_lenght(a : str):
    if len(a) > 10:
        print(f"{a} ha più di 10 caratteri.")
    elif len(a) == 10:
        print(f"{a} ha esattamente 10 caratteri.")
    else:
        print(f"{a} ha meno di 10 caratteri.")