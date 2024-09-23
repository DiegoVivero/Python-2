# Solicitar al usuario que ingrese un texto
texto = input("Ingresa un texto: ")

# Definir las vocales a omitir
vocales = "aeiouAEIOU"

# Crear una nueva cadena omitiendo las vocales
texto_sin_vocales = ''.join([letra for letra in texto if letra not in vocales])

# Mostrar el resultado
print("Texto sin vocales:", texto_sin_vocales)
