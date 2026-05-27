"""
Reto 1: El Validador de Contraseñas (Básico)
Objetivo: Practicar if y else.

Pide al usuario que cree una contraseña usando input().

Si la longitud de la contraseña (len) es menor a 8 caracteres, imprime: "Contraseña muy corta".

Si tiene 8 o más, imprime: "Contraseña aceptada".
"""

Username = input ("Ingrese su nombre de usuario: ")
usernameconfirmed = input ("Confirme su nombre de usuario: ")
PassWord = input ("Ingrese su contraseña (Su contraseña debe tener 8 o mas caracteres para ser valida): ")

#Confirmacion de contraseña
Contador = len(PassWord or PassWordconfirmed)

while len(PassWord) <= 8:
    if len(PassWord) >= 8:
        print ("Su contraseña cumple con los parametros requeridos")

    else:
        print ("Su contraseña no cumple con los parametros requeridos")

    PassWord = input ("Ingrese su contraseña otra vez (Recuerde cumplir los parametros): ")

PassWordconfirmed = ("Confirme su contraseña: ")

print ("Ahora puedes iniciar sesion, Intentalo")

Iniciar_Sesion_Usuario = input ("Introduzca su Nombre de usuario: ")
Iniciar_Sesion_Contraseña = input ("Ingrese su contraseña: ")

# Confirmacion del usuario y contraseña
if Username == Iniciar_Sesion_Usuario and PassWord == Iniciar_Sesion_Contraseña:
    print ("Su usuario a sido validado")
else:
    print ("Su usuario no es valido")