studenti = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]
media = sorted(studenti, key = lambda studente : studente["media"], reverse = True)
print(media)