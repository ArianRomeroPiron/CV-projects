"""
Reto 1: El Conversor de Temperatura

Objetivo: Crear una función que transforme datos y devuelva un resultado.

- Crea una función llamada celsius_a_fahrenheit(c).
- La función debe recibir los grados Celsius como parámetro.
- La fórmula es: $F = (C \times 1.8) + 32$.
- La función debe retornar el resultado.

Extra: Pide al usuario el valor por input(), llama a la función e imprime el resultado.
"""

def celsius_a_fahrenheit():
    if usuario == "F" or usuario == "f":
        F = (Conversor * 1.8) + 32
             
        print ("Tu cambio de Celsius a fahrenheit es de: ", F)

    elif usuario == "C" or usuario == "c":
        C = (Conversor - 32) * 5/9

        print ("Tu cambio de Fahrenheit a Celsius es de: ", C)

    else:
        print ("Ingresaste un dato que no corresponde a las opciones que te dimos, favor de colocar uno de los tipos de datos solicitados")


usuario = str(input("Elija el tipo de Transformacion quiere hacer. si es de celsius a fahrenheit ingrese (F), de ser lo contrario ingrese (C): "))
Conversor = int(input("Coloca la cantidad de grados que quieres transformar: "))

celsius_a_fahrenheit()