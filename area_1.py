# Solicitar ingreso del lado del cuadrado al usuario
lado = float(input("Ingrese el lado del cuadrado: "))
# Calcular el área del cuadrado
area = lado ** 2
# Calcular el area del triangulo equilátero
area_triangulo = ((3 ** (0.5))/4) * (lado ** 2)
# Mostrar resultado
print(f"El área del cuadrado es: {area:.2f}")
print(f"El área del triangulo es: {area_triangulo:.2f}")

