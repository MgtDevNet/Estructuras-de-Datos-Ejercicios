# Vanya walks late at night along a straight street of length l, lit by n lanterns. Consider the coordinate system with the beginning of the street corresponding to the point 0, and its end corresponding to the point l. Then the i-th lantern is at the point ai. The lantern lights all points of the street that are at the distance of at most d from it, where d is some positive number, common for all lanterns.

# Vanya wonders: what is the minimum light radius d should the lanterns have to light the whole street?

# Input
# The first line contains two integers n, l (1 ≤ n ≤ 1000, 1 ≤ l ≤ 109) — the number of lanterns and the length of the street respectively.

# The next line contains n integers ai (0 ≤ ai ≤ l). Multiple lanterns can be located at the same point. The lanterns may be located at the ends of the street.

# Output
# Print the minimum light radius d, needed to light the whole street. The answer will be considered correct if its absolute or relative error doesn't exceed 10 - 9.


import sys

def solve():
    # Lectura rápida de datos
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    l = int(input_data[1])
    
    # Convertimos las posiciones a enteros y las ORDENAMOS
    a = [int(x) for x in input_data[2:]]
    a.sort()  # O(n log n)
    
    # 1. Distancia máxima entre linternas consecutivas
    max_gap = 0
    for i in range(n - 1):
        gap = a[i + 1] - a[i]
        if gap > max_gap:
            max_gap = gap
            
    # 2. Las linternas en los extremos deben cubrir desde 0 y hasta L
    dist_inicio = a[0]
    dist_fin = l - a[n - 1]
    
    # 3. El radio necesario en el centro es max_gap / 2
    # La respuesta es el máximo entre cubrir los bordes y cubrir los centros
    ans = max(max_gap / 2.0, float(dist_inicio), float(dist_fin))
    
    # Imprimimos con alta precisión decimal
    print(f"{ans:.10f}")

if __name__ == '__main__':
    solve()