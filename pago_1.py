# Solicitar ingreso al usuario
precio = int(input("Ingrese el precio: "))
monto_pago = int(input("Ingrese el pago: "))

# Realizar cálculos
vuelto = monto_pago - precio

# Calcular cuantos billetes de a $1.000 se requieren

billetes_1000 = int(vuelto / 1000) 

print(billetes_1000)

# Mostrar el resultado
print(f"El vuelto es {vuelto}")

