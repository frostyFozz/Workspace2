from tkinter import N


palabraSinVocal = ""

userWord = input("Introduce tu palabra: ")
userWord = userWord.upper()


for letra in userWord:
    if letra == "A":
        continue
    if letra == "E":
        continue
    if letra == "I":
        continue
    if letra == "O":
        continue
    if letra == "U":
        continue
    print(letra , end="", )
if letra:
    palabraSinVocal = "vocales"
    print("\nEsta palabra no tiene", palabraSinVocal)

# Imprimir la palabra asignada a palabraSinVocal.
