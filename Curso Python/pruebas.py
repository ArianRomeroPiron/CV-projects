# 1- Funcion del codigo "print"
print ("hello world") #Aqui saldra hello world en la terminal

# 2- Funcion de las variables
Variable_Ejemplo = "Hello world again" 
print (Variable_Ejemplo) #Aqui saldra "Hello world again" en la terminal

# 3- Funcion de los tipos de operadores matematicos
Potencia = 2 ** 3 #Multiplicara el primer numero la cantidad de veces que se coloque en el 2do
Residuo = 22 % 8 #Respondera con lo que sobre de la multiplicacion de los numeros colocados
Divicion_sin_desimales = 22 // 8 #Divide los numero dados, si el resultado es decimal, lo vuelve entero
Division = 22 / 8 #Divide los numeros dados
Multiplicacion = 2 * 5 #Multiplica los numeros dados
Resta = 2 - 3 #Resta los numeros dados
Suma = 2 + 3 #suma los numero dados

print(f"{Potencia}\n{Residuo}\n{Divicion_sin_desimales}\n{Division}\n{Multiplicacion}\n{Resta}\n{Suma}\n")

# 4- Funcion de los tipos de datos
enteros = int(2.5) #Solo dara como resultados numeros enteros, aunque sean decimales
numeros_flotantes = float(2) #Dara numeros flotantes(Decimales), aunque sean enteros
Cadenas = str("Esto es una cadena") #Este almacena texto, si se coloca un numero, lo vera como texto, sin excepciones

print (f"{enteros}\n{numeros_flotantes}\n{Cadenas}")

# 5- Funcion del len
Lector = len('Achicopalado') #Lee la cantidad de dijitos dados dentro de las comillas
print (Lector)

# 6- Funcion del if-else-elif
if Variable_Ejemplo == "Hello world again":
    print ("Hello world again again")

else:
    print ("achicopalado 2")

# 7- modificacion del indice

Lista2 = ["Hola", "a", "Hola"]

for x in range(len(Lista2)):
    if Lista2[x] == "Hola":
        Lista2[x] = "Adios"