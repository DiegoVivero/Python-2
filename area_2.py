# Solicitar ingreso del lado del cuadrado al usuario
lado = float(input("Ingrese el lado del cuadrado: "))
# Calcular el área del cuadrado
area = lado ** 2
# Calcular el area del triangulo equilátero
area_triangulo = ((3 ** (0.5))/4) * (lado ** 2)
# Calcular el área de un pentágono regular
area_pentagono = (lado ** 2 * (25 + 10 * 5 ** (0.5)) ** (0.5))/4
# Mostrar resultado
print(f"El área del cuadrado es: {area:.2f}")
print(f"El área del triangulo es: {area_triangulo:.2f}")
print(f"El área del pentágono es: {area_pentagono:.2f}")