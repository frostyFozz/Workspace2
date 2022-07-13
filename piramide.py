bloques = int(input("Ingrese el número de bloques:"))
altura = 0
base = 1
while altura <= bloques:
    altura += 1
    bloques -= base
    base += 1


print("La altura de la pirámide:", altura)