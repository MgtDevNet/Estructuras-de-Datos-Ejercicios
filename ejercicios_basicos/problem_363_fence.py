import sys

def solve():
    entrada = sys.stdin.read().split() #o(n)
        
    n,k = int(entrada[0]),int(entrada[1])
    h = [int(x) for x in entrada[2:]] #o(n)
    
    # 1. Calculamos la suma de la primera ventana (los primeros k elementos)
    suma_actual = sum(h[:k]) #o(k)
    min_suma = suma_actual
    idx_min = 1  # Guardamos el índice (1-indexed)
    
    # 2. Deslizamos la ventana desde la posición 1 hasta n - k
    for i in range(1, n - k + 1): #o(n)
        # Restamos el elemento que sale (h[i - 1]) y sumamos el que entra (h[i + k - 1])
        suma_actual = suma_actual - h[i - 1] + h[i + k - 1] #o(1)

        #la idea principal es no sumar los k números sino sumar el siguiente y eliminar
        #el primero.

        
        # Si encontramos una suma menor, actualizamos
        if suma_actual < min_suma: #o(1)
            min_suma = suma_actual #o(1)
            idx_min = i + 1  # Convertimos a 1-indexed #o(1)
            
    print(idx_min) #o(1)

if __name__ == '__main__':
    solve() #o(n)