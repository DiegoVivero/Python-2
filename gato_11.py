while True: 
    n = int(input("Ingrese un valor n mayor que 0:  "))
    if n < 0:
        continue
    else:
        break
    miau(n)

def miau(n):
    for i in range(n): 
        print("miau")
main()
