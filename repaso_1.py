# Solicitar ingreso del lado del cuadrado al Usuario

lado = float(input("Ingrese el lado del cuadrado: "))

# Calcular el área del cuadrado

area = lado ** 2

#Calcular el área del triangulo equilatero

area_triangulo = ((3 ** (0.5))/4) * (lado ** 2)

# Mostrar Resultado 

print(f" El area del cuadrado es: {area:.2f} ")
print(f"El area del triangulo es: {area_triangulo:.2f} ")
