# We know that prime numbers are positive integers that have exactly two distinct positive divisors. Similarly, we'll call a positive integer t Т-prime, if t has exactly three distinct positive divisors.

# You are given an array of n positive integers. For each of them determine whether it is Т-prime or not.

# Input
# The first line contains a single positive integer, n (1 ≤ n ≤ 105), showing how many numbers are in the array. The next line contains n space-separated integers xi (1 ≤ xi ≤ 1012).

# Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is advised to use the cin, cout streams or the %I64d specifier.

# Output
# Print n lines: the i-th line should contain "YES" (without the quotes), if number xi is Т-prime, and "NO" (without the quotes), if it isn't.

import sys
import math

def construir_criba(limite):
    """
    Genera un arreglo booleano donde es_primo[i] es True si i es primo.
    Usa la Criba de Eratóstenes en O(N log(log N)).
    """
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos
    
    for i in range(2, int(math.isqrt(limite)) + 1):
        if es_primo[i]:
            # Marcamos todos los múltiplos de i como no primos
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False
                
    return es_primo

def solve():
    # 1. Criba precalculada hasta 1,000,000 (raíz cuadrada de 10^12)
    MAX_RAIZ = 1000000
    es_primo = construir_criba(MAX_RAIZ)
    
    # 2. Entrada rápida
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    numeros = input_data[1:]
    
    resultados = []
    
    # 3. Procesamos cada número en O(1)
    for x_str in numeros:
        x = int(x_str)
        
        # math.isqrt da la raíz cuadrada entera exacta sin problemas de flotantes
        r = math.isqrt(x)
        
        # Debe ser un cuadrado perfecto Y su raíz debe ser un número primo
        if r * r == x and es_primo[r]:
            resultados.append("YES")
        else:
            resultados.append("NO")
            
    # 4. Impresión rápida masiva
    sys.stdout.write('\n'.join(resultados) + '\n')

if __name__ == '__main__':
    solve()
        
        
        

    
