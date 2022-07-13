from tkinter import N


num1 = input("Ingresa un el numero para la operacion: ")
try:
    num1 = int(num1)
except:
    num1 = 'hola'
    exit()

num2 = input('Ingresa tu segundo numero: ')
try:
    num2 = int(num2)
except: 
    num2 = 'Edwin'
    exit()

operador = input("Ingresa el simbolo para la operacoin: ")
if operador == "+" :
    print( "el resultado es", num1 + num2 )
elif operador == "-" :
    print( "el resultado es", num1 - num2 )
elif operador == "*" :
    print("el resultado es ", num1 * num2)
elif operador == "/" :
    print("El resultado es ", num1 / num2)
else:
    print("No has introducido los valores correctos")
    exit()

print("\n¡Eso es todo, amigos!")
