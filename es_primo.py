def es_primo(n):
    for i in range(2, n):
        if n % i == 0: 
            return False
        return True

es_primo = es_primo(7)
if es_primo:
    print("El número es primo")
else: 
    print("El número no es primo")