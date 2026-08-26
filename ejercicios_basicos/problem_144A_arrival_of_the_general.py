import sys

def solve():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    
    n = int(entrada[0])
    a = [int(x) for x in entrada[1:]]
    
    val_max = max(a)
    val_min = min(a)
    
    # primer índice del valor máximo (más a la izquierda)
    idx_max = a.index(val_max)
    
    # último índice del valor mínimo (más a la derecha)
    # recorremos al revés para encontrar la última aparición fácilmente
    idx_min = (n - 1) - a[::-1].index(val_min)
    
    pasos = idx_max + (n - 1 - idx_min)
    
    # Si el máximo estaba después del mínimo, restamos 1 por el cruce
    if idx_max > idx_min:
        pasos -= 1
        
    print(pasos)

if __name__ == '__main__':
    solve()