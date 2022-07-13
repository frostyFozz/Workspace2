numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero = int(input("Introduce el numero secreto: "))

while numero != 777:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    numero = int(input("Introduce el numero secreto: "))
    
if numero == 777:
    print("¡Bien hecho, muggle! Eres libre ahora")