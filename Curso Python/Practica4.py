"""

El Reto: Gestión de Inventario "La Pythonería"
Instrucciones:
Debes crear un programa que permita gestionar los productos de una tienda. El programa debe seguir estas reglas:

Configuración Inicial:

Crea una lista llamada productos que empiece vacía.

Crea una variable presupuesto con un valor de 100.0.

El Menú Principal (Bucle while):

El programa debe mostrar un menú infinito hasta que el usuario elija "Salir".

Opciones: 1. Agregar Producto, 2. Ver Inventario, 3. Salir.

Lógica de "Agregar Producto" (if + input):

Pide el nombre del producto.

Validación con len(): Si el nombre tiene menos de 3 letras, imprime un error y no lo agregues.

Pide el precio (usa float).

Validación de presupuesto: Si el precio es mayor al presupuesto actual, dile al usuario que no tiene dinero suficiente.

Si todo es correcto:

Resta el precio al presupuesto.

Agrega el nombre del producto a la lista productos.

Lógica de "Ver Inventario" (Bucle for):

Muestra el saldo actual del presupuesto.

Usa un bucle for para imprimir cada producto de la lista.

Si la lista está vacía (puedes saberlo con len(productos) == 0), informa que no hay productos.
"""

productos = []
presupuesto = 100.0

while True:
    print("\n--- MENÚ DE LA TIENDA ---")
    
    print ("""
            Agregar producto (1)
            Ver Inventario (2)
            Salir (3)
            """)
    
    opcion = (input("Ingrese uno de los numeros que se le a indicado en el menu para poder comenzar con su inventario: "))
    
    if opcion == "1":
        nombre = input("Nombre del producto: ")
        # Aquí aplicas el len(nombre) y la lógica del dinero...

        productos.append(nombre)

        if len(nombre) <= 3:
            print ("El nombre de su producto debe tener mas de 3 caracteres para ser agregado")

        else:
            restante = float(input("Cuanto sera el precio que costara su producto? (Recuerad que no puedes pasar de tu presupuesto): "))
            
            if restante <= presupuesto:
                presupuesto = presupuesto - restante

                print ("Perfecto, tu producto a sido agregado con exito, tu presupuesot ahora es de: ", presupuesto)

    elif opcion == "2":
        # Aquí usas el for producto in productos...
        
        print ("Tu presupuesto es de: ", presupuesto)

        if len(productos) == 0:
            print ("No hay productos agregados")

        else:
            print ("----LISTA DE PRODUCTOS----")
            
            for i in productos:
                print (i)


    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida")
