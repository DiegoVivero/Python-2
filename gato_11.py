while True: 
    n = int(input("Ingrese un valor n mayor que 0:  "))
    if n < 0:
        continue
    else:
        break

def miau(n):
    for i in range(n): 
        print("miau")

miau(n)