#Escercizio 1-1
#x: float = 2.755
#y: float = 1.0/x
#print(x)
#print(y)

#prodotto: float = x * y
#print (prodotto)


#Esercizio 1-2

#x: float = 2.678
#y: float = x % 2.0

#print(x)
#print(y)


#Esercizio 1-3
#x: int = 45
#y: int = 481
#z: int = 69

#sum = x + y + z
#print(sum)
#media = sum/3
#print(media)


#Eserecizi 1-4
#num: int = input("Inserire numero:")
#for cifra in num:
#    print(cifra)


#Esercizio 1-5
#gradiF = int(input("Inserire gradi Fahrenheit: "))
#conversione : float = 5 * (gradiF - 32) / 9
#print(f"Risultato convertito in gradi Celsius {conversione:.1f}°")


#Esercizio 1-6
#menu: dict = {"Pizza": 9.00, "Pasta": 10.50, "Zuppa": 7.00, "Hamburger": 15.50, "Cotoletta": 10.00, "Salmone": 20.20, "Patatine Fritte": 5.50, "Patate al forno": 5.50, "Verdura del giorno": 7.00, "Cheesecake": 6.00, "Tiramisu": 6.00, "Focaccia con nutella": 6.00, "Coca": 3.50, "Acqua": 1.50, "Vino": 5.00}
#print(menu)

#ordine: dict = {"Pasta", "Cotoletta", "Patatine Fritte", "Cheesecake"}

#totale = 0

#for piatto in ordine:
#    totale += menu[piatto]
#print(f"{totale:.2f}")


#Esercizio 2-3
#name: str = "Antonio"
#print(f"Hello {name}, would you like to learn some Python today?")


#Esercizio 2-4
#name: str = "Antonio"
#print(name.upper())
#print(name.lower())
#print(name.title())


#Esercizio 2-5
#print("James Bond una volta disse:\"Il mio nome è Bond, James Bond\".")


#Esercio 2-6
#famous_person: str = "James Bond"
#print(f"{famous_person} una volta disse: \"Il mio nome è Bond, James Bond\".")


#Esercizio 3-1
#lista_1: list = ["Matteo", "Luca", "Francesco", "Lorenzo", "Francesco"]
#print(lista_1[0])
#print(lista_1[1])
#print(lista_1[2])
#print(lista_1[3])


#Esercizio 3-2
#print("Ciao "+ lista_1[0]+ " come te la passi?")
#print("Ciao "+ lista_1[1]+ " come te la passi?")
#print("Ciao "+ lista_1[2]+ " come te la passi?")
#print("Ciao "+ lista_1[3]+ " come te la passi?")


#Esercizio 3-3
#trasporto: list = ["Moto", "Macchina", "Camion", "Camper"]
#print("Mi piacerebbe tanto avere una "+ trasporto[0] +" sgravata!")
#print("Vorrei prendere la patente per giudare il " + trasporto[3] + ", così posso girare il mondo!")


#Esercizio 3-4




# Esercizio Mario kart (mio)
# i : int = 0

# while i < 10:
#     opzione = int(input("Inserire posizionamento: "))
#     if opzione == 0 or opzione > 10:
#         print("Posizione non valida. \n Inserire una posizione valida.")
#         continue
#     if opzione == 1:
#         print(f"Finishing position: {opzione} \n {opzione}st")
#     elif opzione == 2:
#         print(f"Finishing position: {opzione} \n {opzione}nd")
#     elif opzione == 3:
#         print(f"Finishing position: {opzione} \n {opzione}rd")
#     else:
#         print(f"Finishing position: {opzione} \n {opzione}th ")
#     i += 1
# print("Posti in classifica terminati.")