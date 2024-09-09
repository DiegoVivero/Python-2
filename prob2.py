L = float(input("Ingrese el lado de un poligono regular: "))

area_cuadrado = L ** 2 
area_triangulo = ((3)**(0.5))*(L ** 2)/4
area_pentagono = (L ** 2)*(25 + 10 * (5 ** 0.5)) ** 0.5 /4

print(f"Ingrese area del cuadrado: {area_cuadrado:.2f}")
print(f"Ingrese area del triangulo: {area_triangulo:.2f}")
print(f"Ingrese area del pentagono: {area_pentagono:.2f}")

