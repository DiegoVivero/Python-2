# Solicitar ingreso al usuario
precio = int(input("Ingrese el precio: "))
monto_pago = int(input("Ingrese el pago: "))

# Realizar cálculos
vuelto = monto_pago - precio

# Calcular cuantos billetes de a $1.000 se requieren
billetes_1000 = int(vuelto / 1000) 
vuelto = vuelto - (billetes_1000 * 1000) #Vuelto % 1000

# Calcular cuantos billetes de a $500 se requieren 
monedas_500 = int(vuelto / 500)

# Mostrar el resultado
print(f" {billetes_1000} billetes de $1.000")
print(f" {monedas_500} monedas de $500")

