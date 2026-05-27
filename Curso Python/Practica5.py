Palabra = int(input("Ingrese una palabra: "))

Original = Palabra

print("La palabra original es: " + Palabra)
print("La palabra invertida: " + Palabra[::-1])   

Invertida = Palabra[::-1]

if Palabra == Invertida:
    print ("Tu palabra invertida es igual a como estaba originalmente. Esta palabra es palíndromo")

else:
    print ("Tu palabra de manera invertida es diferente a la original")