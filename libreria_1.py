num_clientes = int(input("ingresar número de clientes: "))
venta_del_dia = 0
for i in range(num_clientes):
    nombre = input("cual es tu nombre: ")

    cocina = int(input("cuantos libros de cocina quiere: "))
    arte = int(input("cuantos libros de arte quiere: "))
    religioso = int(input("cuantos libros religioso quiere: "))
    novelas = int(input("cuantos libros de novelas quiere: "))

    #Precios
    p_cocina = 5500
    p_arte = 4500
    p_religioso = 6500
    p_novelas = 5000

    precio_total = cocina * p_cocina + arte * p_arte + religioso * p_religioso + novelas * p_novelas
    venta_del_dia += precio_total

    print(f"El precio total del pedido para {nombre} es: {precio_total}")

    if cocina >=1 and arte >=1 and religioso >=1 and novelas >=1:
        descuento = 0.20
    elif (cocina <=1 or arte <=1 or religioso <=1 or novelas <=1) and (cocina + arte + religioso + novelas) == 2:
        descuento = 0.15
    elif cocina == 4 or arte == 4 or religioso == 4 or novelas == 4:
        descuento = 0.10
    elif cocina == 2 or arte == 2 or religioso == 2 or novelas == 2:
        descuento = 0.05
    else:
        descuento = 0.0

    print(f"El precio total con descuento de {descuento * 100}% es igual a: {precio_total * (1 - descuento)}")
    venta_del_dia += precio_total * (1 - descuento)

print(f"El cliente que mas libros compro fue: max{nombre}")
