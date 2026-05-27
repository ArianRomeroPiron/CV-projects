"""
Reto 2: El Cajero Automático (Uso de while)
Objetivo: Mantener el programa funcionando hasta que el usuario decida salir.

Crea una variable saldo = 1000.

Usa un bucle while True para mostrar un menú infinito:

Ver saldo.

Retirar dinero.

Salir.

Si el usuario elige "Salir", usa break para terminar el programa.

Si elige "Retirar", resta la cantidad del saldo (solo si tiene suficiente dinero).
"""

Saldo = 1000

while True:

    print (""" 
            - Ver saldo.
            - Retirar dinero.
            - Salir. 
           """)
    
    Opcion = input("Ingresa la accion que quieres realizar a continuacion: ")

    if Opcion == "Saldo" or Opcion == "saldo":
            print ("Tu saldo es de: ", (Saldo))

            continue

    elif Opcion == "Retirar" or Opcion == "retirar":
        if Saldo > 0:
            
            Retiro = int(input("Ingresa la cantidad a retirar:"))

            Saldo = Saldo - Retiro

            print ("Haz retirado: ", Retiro, "$ Pesos, revisa tu monto para ver cuanto mas puedes retirar")

        else:
            print ("No tienes el monto suficiente para retirar, Tendras que ingresar dinero")

    else:
        break
        