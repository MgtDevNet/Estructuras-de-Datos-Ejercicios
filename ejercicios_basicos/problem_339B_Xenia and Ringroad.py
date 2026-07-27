import sys

def solve():
    entrada = sys.stdin.read().split() #o(1)
    n = int(entrada[0]) #o(1)
    m = int(entrada[1]) #o(1)
    a = [1]+list(map(int,entrada[2:])) #o(m)
    #print(a)
    c = 0
    for i in range(m):#o(m)
        #print(a[i])
        if a[i] <= a[i+1]: #o(1)
            c += a[i+1]-a[i] #o(1)
        else:
            c += a[i+1]-a[i]+n #o(1)

    #print()
    print(c) #o(1)

if __name__ == '__main__':
    solve()

#finalmente es o(m)

#hay una manera más optima y sin necesidad de usar los condicionales


def solve():
    # Creamos un iterador para consumir datos sin crear sublistas en RAM
    it = iter(sys.stdin.read().split())
    
    primer_dato = next(it, None)
    if primer_dato is None:
        return
        
    n = int(primer_dato)
    m = int(next(it))
    
    pasos_totales = 0
    pos_actual = 1  # Xenia siempre empieza en la casa 1
    
    # Procesamos cada una de las m tareas
    for _ in range(m):
        pos_siguiente = int(next(it))
        
        # Fórmula limpia para distancia circular
        pasos_totales += (pos_siguiente - pos_actual + n) % n
        
        # Avanzamos la posición
        pos_actual = pos_siguiente
        
    print(pasos_totales)

if __name__ == '__main__':
    solve()

# Nota a tener en cuenta: La razón lógica para eliminar los condiconales
# es que es fácil pensar el problema como un círculo y las casas
# enumeradas con la orientación del reloj.
# 
# Supongamos que hay 5 casas, n = 5. Si se quiere ir de la 2 a la 4 - son 2 pasos - si
# se quiere pasar de la 4 a la 2 sería -2 pasos que no se puede, ahora bien, seria: 4-5,5-1,1-2
# osea 3 pasos, que básicamente sería 2-4+5 = 3 - siguiente-actual+hogares-. A esa formula puede
# llegarse pensando de la siguiente manera: 

#   Estoy en el 4, pero primero debo darle la vuleta al reloj, entonces
#   para llegar al final sería 5-4=1 pasos, luego a eso le sumo la distancia desde
#   1 hasta donde quiero ir en este caso, 2-1 =1 y a eso, le sumo el paso de 5 a 1.
#   Así llego al 3. 
# 
# Osea (4-5) + (2-1) + (1) que por asociatividad sería 4-2+5. Ahora bien, Este caso es 
# para pasar de un número mayor a uno menor y por eso se suma 5, la forma de que sea al revez y sea
# pasar de un número menor a uno mayor - 2 a 4 por ejemplo- solo sería 4-2, osea, quitar ese 5 y para que eso
# pase sin necesdad de tener un condicional sería con el módulo.
# 
# porque 2-4+5 = 3 mod 5 = 3 y 4-2+5 = 7 mod 5 = 2. De tal manera que se puede tener
# una sola formula para 2 casos.  
