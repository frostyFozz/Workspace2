import math


import math

print("Este programa sirve para imprimir la raiz de un numero entero")
numero = int(input("Introduce un numero: "))
intentos = 0

while numero<0:
    print("Introdugiste un numero negativo, no se puede encontrar la raiz de este")

    if intentos == 2:
        print("haz agotado todos tus intentos el programa ha finalizado")
        break;

    numero = int(input("Introduce un numero:"))
    if numero<0:
        intentos = intentos +1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz de un numero entero es igual" + str(numero) + "esta es la raiz de este numero" + str(solucion))
