anio = int(input("Introduzca un año:"))
if anio % 4 != 0:
    print("El anio no es bisiesto")
elif anio % 4 == 0 and anio % 100 != 0:
    print("El anio es bisiesto")
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0:
    print("El anio no es bisiesto")
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0:
    print("El anio es bisiesto")

    #este codigo se utiliza para saber si un anio es bisiesto o no