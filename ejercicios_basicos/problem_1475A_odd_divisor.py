import sys
import math

t = int(sys.stdin.readline()) #o(1)
for i in range(t): #o(t)
    n = int(sys.stdin.readline()) #o(1)
    
    if (n & 1 != 0):#o(1)
        print("YES")#o(1)
    else:
        if math.log2(n).is_integer():#o(1)
            print("NO")#o(1)
        else:
            print("YES")#o(1)
        
#finalmente, la complejidad final es de o(t)


def solve():
    # Leer todas las líneas de golpe para Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    resultados = []
    
    # Procesamos cada n de forma O(1) pura y segura
    for i in range(1, t + 1):
        n = int(input_data[i])
        
        # Si es impar (n & 1 != 0), la respuesta es YES.
        # Si NO es potencia de 2 (n & (n - 1) != 0), la respuesta es YES.
        if (n & 1 != 0) or (n & (n - 1) != 0):
            resultados.append("YES")
        else:
            resultados.append("NO")
            
    # Un solo print para todos los casos: O(t) en escritura ultra veloz
    sys.stdout.write('\n'.join(resultados) + '\n')

if __name__ == '__main__':
    solve()