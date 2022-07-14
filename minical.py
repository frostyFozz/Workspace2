
def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def multi(num1, num2):
    return num1 * num2
def divicion(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0 !!")

def entero(num1, num2):
    try:
        return num1 // num2
    except ZeroDivisionError:
        print("Las diviciones entre 0 no estan disponibles")

num1 = input("Ingresa un el numero para la operacion: ")
num2 = input('Ingresa tu segundo numero: ')
operador = input("Ingresa el simbolo para la operacoin: ")


try:
    num1 = int(num1)
except:
    num1 = ("hola")
    exit()
try:
    num2 = int(num2)
   
except:
    num2 = ("edwin")
    exit()
 

if operador == "suma" :
    print(suma(num1, num2 ))
elif operador == "resta" :
    print(resta(num1, num2 ))
elif operador == "multi" :
    print(multi(num1, num2))
elif operador == "divicion" :
    print(divicion(num1, num2))
elif operador == "entero" :
    print(entero(num1, num2))

    
else:
    print("No has introducido los valores correctos")

print("\n¡Eso es todo, amigos!")
