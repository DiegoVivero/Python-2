# Solicitar al usuario que ingrese una moneda

moneda = int(input("Ingrese una moneda de 25, 10 o 5 centavos: "))
monedas_aceptadas = [25, 10, 5]
saldo = 50 
while saldo > 0:
    print(f"Monto saldo: {saldo} centavos")
    moneda = int(input("Ingrese moneda de 25, 10, 5 centavos: "))

    #Preguntar si las monedas es aceptada
    if moneda in monedas_aceptadas: 
        saldo = saldo - moneda
    else: 
        print("Insertar solo monedas de 25, 10 o 5 centavos ")

if saldo == 0: 
    print(f" su vuelto es: {abs(saldo)} centavos")
else: 
    print("Gracias!")



