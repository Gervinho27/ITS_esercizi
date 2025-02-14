# # esercizio1 
# import math
# a = int(input("Inserire a: "))
# b = int(input("Inserire b: "))
# if a > b:
#     c = math.sqrt(a ** 2 - b ** 2)
#     print(f"Il cateto è lungo {c} cm luca muore domani  :)")
# else:
#     print("Errore")

# esercizio 2

# max = int(input("Inserire numero: "))
# i: int =  1 
# while i < 4: 
#     n = int(input("Inserire numero: "))
#     i += 1
#     if  n > max: 
#         max = n 
# print(f"Il massimo tra i 4 numeri è {max}")

# esercizio 3

# sum: int = 0 
# i: int = 1 
# while i < 5:
#     n = int(input("Inserire numero: "))
#     if n > 0: 
#         sum += n
#     else:
#         print("Numero non valido")
#     i += 1
# print(f"La somma è {sum}")

# esercizio 4

# n = int(input("Inserire numero: "))
# if n % 2 == 0:
#     print(f"{n} è un numero pari")
# else:
#     print(f"{n} non è un numero pari")

# esercizio 5 

# primo: bool = True
# n = int(input("Inserire numero: "))
# if n < 2:
#     print(" non è un  numero primo")
# else:
#     div = 2 
#     while div < n:
#         if n % div == 0:
#             print("Il numero non è primo") 
#             div += 1
#             primo: bool = False 
#             break 
# if primo:           
#    print("Il numero è primo")

# esercizio 6

# n = int(input("Inserire numero: "))
# if n > 0:
#     fattoriale: int = 1
#     i: int = 1
#     for i in range(1, n + 1):
#         fattoriale = fattoriale * i
# print(fattoriale)

# esercizio 7 

# pari: int = 0
# dispari: int = 0
# i: int = 0
# while i < 10:
#     n = int(input("Inserire numero: "))
#     if n % 2 == 0: 
#         pari += 1
#     else:
#         dispari += 1
#     i += 1
# print(f"I numeri pari sono {pari}, e i dispari sono {dispari}")

# esercizio 8 

# n = int(input("Inserire valore soglia: "))
# i: int = 1
# while i <= 7:
#     z = int(input("Inserire luca succhia cazzi: "))
#     if z > n:
#         print(z)
#     i = i + 1


# esercizio 9 
# nome = str(input("Inserire nome venditore: "))
# vendite = int(input("Inserire vendite: "))
# max_nome: str = nome
# max: int = vendite
# min_nome: str = nome
# min: int = vendite
# i = 0
# while i < 20:
#     new_nome = str(input("Inserire nuovo nome venditore: "))
#     new_vendita = int(input("Inserire nuovo totale: "))
#     if new_vendita > max:
#         max_nome = new_nome
#         max = new_vendita
#     elif new_vendita < min:
#         min_nome = new_nome
#         min = new_vendita
#     i = i + 1
# print(max_nome, max)
# print(min_nome, min)

# esercizio 10 

# reddito = int(input("Inserire reddito: "))
# media= int(input("Inserire media: "))
# if reddito < 20000 and media > 27:
#     print("Borsa di studio approvata!!")
# elif reddito > 20000:
#     print("Borsa di studio non approvata perchè hai troppi soldi")
# else:
#     print("Borsa di studio rifiuta perche hai la media troppo bassa.")

#esercizio 11

# sedie_libere = 20
# sedie_occupate = 0
# opzione: str = ""
# while opzione != "esci":
#     opzione = str(input("Che vuoi fare: "))
#     if opzione == "prenota":
#         if sedie_libere> 0:
#             sedie_libere -= 1 
#             sedie_occupate += 1
#         else:
#             print("Non ci sono sedie disponibili!")
#     if opzione == "libera":
#         if sedie_libere < 20:
#             sedie_libere +=1
#             sedie_occupate -= 1
#         else:
#             print("tutte le sedie sono gia libere!")
#     if opzione == "visualizza":
#         print(f"Le sedie libere sono {sedie_libere} e quelle occupate sono {sedie_occupate}")



# esercizio 12

# parcheggi_max = int(input("Inserire posti massimi: "))

# posti_liberi: int = parcheggi_max
# opzione: str = ""
# while opzione != "esci":
#     opzione = str(input("Che vuoi fare amigo (colui che parla è una parcheggiatore abusivo): "))
#     if opzione == "ingresso":
#         if posti_liberi > 0:
#             posti_liberi -= 1
#         else:
#             print("Il parcheggio è pieno")
#     if opzione == "uscita":
#         if posti_liberi < parcheggi_max:
#             posti_liberi += 1
#         else:
#             print("Tutti i parcheggi sono gia libere")
#     if opzione == "stato":
#         print(f"I posti liberi sono {posti_liberi} e i posti occupati sono {parcheggi_max - posti_liberi}")        
#     else:
#         print("Amigo non capisco")

# esercizio 13 

# auto_NS = int(input("Inserire macchine che vegono da NS: "))
# auto_EO = int(input("Inserie macchine che vengono da EO: "))
# soglia = int(input("Inserire soglia: "))
# tempo_priorita = int(input("Inserire tempo priorita: "))
# tempo: int = 100
# if auto_NS > soglia:
#     if auto_EO > soglia:
#          tempo_NS = 50
#          tempo_EO = 50
#     else:
#         tempo_NS = tempo_priorita
#         tempo_EO = tempo - tempo_priorita
# else:
#     if auto_EO > soglia:
#         tempo_EO = tempo_priorita
#         tempo_NS = tempo - tempo_priorita
#     else:
#         veicoli_tot = auto_NS + auto_EO
#         tempo_NS = auto_NS / veicoli_tot
#         tempo_EO = tempo - tempo_NS
# print(f"Il tempo assegnato alle auto NS è {tempo_NS} e il tempo assegnato alle auto EO è {tempo_EO}.")

#esercizio 14

# corso = str(input("Quale corso vorresti frequentare?: "))
# posti: int = 100
# opzione: str = None
# while opzione != "esci":
#     opzione = str(input("Inserire opzione: "))
#     if opzione.title() == "Iscriviti":
#         if posti > 0:
#             posti -= 1
#             print("Sei iscritto!!")
#         else:
#             print("Non ci sono posti disponibili")
#     elif opzione == "annulla":
#         if posti < 100:
#             print("Hai annullato l'iscrizione...")
#             posti +=1
#         else:
#             print("tutti i posti sono gia disponibili")
#     elif opzione == "visualizza":
#         print(f"I posti disponibili sono {posti} e i posti rimasti sono {100 - posti}")
#     else:
#         print("Inserire un opzione valida!")

# esercizio 15


# tutor: int = 2
# attesa: int = 0
# status: bool = True
# while status:
#     studente = str(input("Inserire studente: "))
#     if tutor > 0:
#         tutor -= 1
#         print("Tutor assegnato correttamente!")
#     else:
#         attesa += 1
#         print("Assegnato a lista di attesa")
#     if tutor == 0 and attesa == 3:
#         status: bool = False
# print("Posti esauriti!")

# esercizio 16

# sum: int = 0
# n = int(input("Inserire numero: "))
# if n % 1 == 0 and n > 0:
#     i = 1 
#     sum: int = 0
#     for i in range(1, n + 1):
#         sum = sum + i**2
# else:
#     print("Inserire un numedo valido!")
# print(sum)

# esercizio 17

# sum: int = 0
# i: int = 1
# x = int(input("Inserire numero positivo: "))
# if x > 0:
#     while i < 10:
#         n = int(input("Inserire numero: "))
#         if x % 2 == 0:
#             if n > x / 2:
#                 sum += n
#         else:
#             if n < x:
#                 sum += n
#         i += 1
#     print(sum)
# else:
#     print("Io ti avevo avvisato!")

# esercizio 18

# voti: int = 0
# sum: int = 0
# scelta: str = None
# while scelta != "no":
#     scelta = str(input("Vuole inserire un voto?: ")).lower()
#     if scelta == "si":
#         voto = int(input("Inserire voto: "))
#         if voto > 0:
#             voti += 1
#             sum += voto
#         else:
#             print("Inserire un voto valido")
# media: int 
# if voti > 0:
#     media = sum / voti
#     print(media)