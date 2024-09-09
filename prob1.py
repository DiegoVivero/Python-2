input("Bienvenidos")

precio = int(input("Ingrese el precio del producto: "))
pago = int(input("Ingrese el monto de pago con el que pago: "))

vuelto = pago - precio 

billete_20000 = int(vuelto / 20000)
vuelto = vuelto - (billete_20000 * 20000) 
print(billete_20000, "billetes de $20.000")

billete_10000 = int(vuelto / 10000)
vuelto = vuelto % 10000
print(billete_10000, "billetes de $10.000")

billete_5000 = int(vuelto / 5000)
vuelto = vuelto % 5000
print(billete_5000, "billetes de $5.000")

billete_2000 = int(vuelto / 2000)
vuelto = vuelto % 2000
print(billete_2000, "billetes de $2.000")

billete_1000 = int(vuelto / 1000)
vuelto = vuelto % 1000
print(billete_1000, "billetes de $1.000")

monedas_500 = int(vuelto / 500)
vuelto = vuelto % 500
print(monedas_500, "Monedas de $500")

monedas_100 = int(vuelto / 100)
vuelto = vuelto % 100
print(monedas_100, "Monedas de $100")

monedas_50 = int(vuelto / 50)
vuelto = vuelto % 50
print(monedas_50, "Monedas de $50")

monedas_10 = int(vuelto / 10)
vuelto = vuelto % 10
print(monedas_10, "Monedas de $10")
