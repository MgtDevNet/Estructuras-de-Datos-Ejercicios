import sys

def solve():
    it = iter(sys.stdin.read().split()) #o(1) constante
    n = int(next(it)) #o(1)
    m = int(next(it)) #o(1)
    a = int(next(it))#o(1)
    b = int(next(it)) #o(1)
    resultado=[]#o(1)

    if n == 1: #o(1)
        resultado.append(min(a,b))#o(1)
    elif n%m == 0: #o(1)
        r1 = b*(n//m) #o(1)
        r2 = n*a #o(1)
        resultado.append(min(r1,r2)) #o(1)
    else:
        if m > n:#o(1)
            r1 = a*n #o(1)
            r2 = b #o(1)
            resultado.append(min(r1,r2))#o(1) 
        else:
            c = 0 #o(1)
            for i in range(m,n+m,m): #o(n)
                if i>n: #o(1)
                    c = i-m #número de viajes posibles #o(1)
                    #c//m sería el número de tickets
                    break#o(1)
            r1 = ((c//m)*b)+((n-c)*a)#o(1)
            r2 = ((c+m)//m)*b#o(1)
            resultado.append(min(r1,r2))#o(1)
    print("".join(list(map(str, resultado))))#o(1)
if __name__=='__main__':
    solve()

#finalmente, la complejidad final es o(n)


# Forma de hacerlo en o(1)

import sys

def solve():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
        
    n, m, a, b = map(int, entrada)
    
    # 1. Comprar todo con boletos individuales
    costo_individuales = n * a
    
    # 2. Usar abonos para la mayoría y completar con individuales
    costo_mixto = (n // m) * b + (n % m) * a
    
    # 3. Comprar solo abonos (incluso si el último se desaprovecha un poco)
    # n // m + (1 si n % m != 0 else 0)
    costo_solo_abonos = ((n + m - 1) // m) * b
    
    # La respuesta es el mínimo de las 3 opciones posibles
    print(min(costo_individuales, costo_mixto, costo_solo_abonos))

if __name__ == '__main__':
    solve()

# ES ACONCEJABLE PRIMERO PENSAR EN TODOS LOS CASOS
# POSIBLES PARA LUEGO SACAR UNA FORMULA Y YA, SIMPLEMENTE 
# SACAR EL MÍNIMO. NO ESTA MAL USAR LOS CONDICIONES
# PERO MUCHAS VECES SOLO SON UN ESTORBO. EL USO DEL MÓDULO
# ES BASTANTE PODEROSO