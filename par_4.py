def main():
    x = int(input("¿Qué es x?  "))
    if es_par(x):
        print("es número par")
    else:
        print("Impar")
    
def es_par(n): 
        return n % 2 == 0 
    
main()