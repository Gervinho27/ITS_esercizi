lista_messaggi = ["Ciao, come va?", "Domani pizza?", "Ho il telefono scarico, ti richiamo dopo.", "Porta due birre!"]

def send_message(messaggi):
    sent_message = []
    upper_bound = len(messaggi)
    for i in range(upper_bound):
        message = messaggi.pop(0)
        sent_message.append(message)
        print(f"{messaggi=}\n {sent_message=}\n")

send_message(lista_messaggi)