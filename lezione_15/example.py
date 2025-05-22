PATH: str = "lezione_15/example.txt"
mode : str = "r"
encoding : str = "utf-8"

file = open(PATH, mode=mode, encoding=encoding)

print(file)

output : str = file.write("Hello world!\n")
print(output)
file.close()

