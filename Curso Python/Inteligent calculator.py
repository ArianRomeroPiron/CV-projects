"""
Calculadora inteligente

Qué incluir:

Suma, resta, multiplicación, división
Validación de errores (ej: dividir entre 0)
Menú interactivo
Que funcione en bucle (hasta que el usuario salga)

Extra (si te da tiempo):

Potencias
Raíz cuadrada
Historial de operaciones

"""
calculos = []

while True:
    print ("--- Calculadora Inteligente ---")
    print ("""
       
        Calcular (1)
        Ver Historial de Calculo (2)
        Salir (3)
       
       """)

    opcion = int(input("Ingresa el numero a evaluar dependiendo que accion quieras hacer: "))

    if opcion == 1:
        operacion = str(input("Escribe el tipo de operacion que quieres hacer (Suma, Resta, Multiplicacion, Division): "))
        num1 = int(input("Ingrese el primer digito: "))
        num2 = int(input("Ingrese el segundo digito: "))

        if operacion == "Suma" or operacion == "suma":
            Resultado = num1 + num2

            print (Resultado)
            calculos.append(Resultado)

        elif operacion == "Resta" or operacion == "resta":
            Resultado = num1 - num2

            print (Resultado)
            calculos.append(Resultado)
    
        elif operacion == "Multiplicacion" or operacion == "multiplicacion":
            Resultado = num1 * num2

            print (Resultado)
            calculos.append(Resultado)

        elif operacion == "Division" or operacion == "division":
            Resultado = num1 / num2

            if operacion == "Division" and num1 == 0 or operacion == "division" and num1 == 0 or operacion == "Division" and num2 == 0 or operacion == "division" and num2 == 0:
                print ("Math Error")
                break
            print (Resultado)
            calculos.append(Resultado)

    elif opcion == 2:

        print ("--- Historial de Operaciones ---")

        for i in calculos:
            print (f"-- {i}")

    elif opcion == 3:
        break
