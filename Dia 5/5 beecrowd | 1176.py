from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    
lista = []
n = int(input())

for i in range(n):
    numero = int(input())
    lista.append(fibonacci(numero))
    print(f"Fib({numero}) = {lista[i]}")