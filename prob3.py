n = int(input("Ingresa un número entero positivo: ")) 

es_primo = True

for i in range(2, n): 
    resto = n % i 
    if resto == 0:
        es_primo = False 
        break

    if es_primo: 
        print(f"{n} es primo")
    else:
        print(f"{n} no es primo")

