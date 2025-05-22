studenti : tuple[str] = [("Luca", 21), ("Anna", 19), ("Marco", 22)]
sorted_by_age_ : tuple[str] = sorted(studenti, key=lambda studenti : studenti[1])
print(sorted_by_age_)