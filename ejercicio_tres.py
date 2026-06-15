 # Ejercicio 3
frase = input("Ingresa una frase: ")
if "triste" in frase:
    nueva_frase = frase.replace("triste", "feliz")
    print(nueva_frase)
else:
    print(frase.upper())