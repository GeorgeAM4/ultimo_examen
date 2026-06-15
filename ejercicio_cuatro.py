 #EJERCICIO 4
contrasena = input("Ingresa una contraseña: ").strip()
while contrasena == "12345":
    contrasena = input("Contraseña insegura, ingresa otra: ").strip()
if contrasena != "12345":
    print("Acceso concedido")
else:
    print("Acceso denegado")