import sys

def solve():
    entrada = sys.stdin.read().split() #o(1)
     
    n = int(entrada[0]) #o(1)
    h = int(entrada[1]) #o(1)
    a = list(map(int, entrada[2:])) #o(n)
    
    respuesta = list(map(lambda x: 1 if x<=h else 2, a)) #o(n)
    print(sum(respuesta))
if __name__ == "__main__":
    solve()

#complejidad final O(n)

#una forma de hacerlo sin gastar tanta ram por crear tantas listas
#igualmente es O(n)
import sys


def solve():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    n, h = int(entrada[0]), int(entrada[1])

    # 1 si x <= h, 2 si x > h es equivalente a: 1 + (x > h)
    # En Python, True equivale a 1 y False a 0
    ancho_total = sum(1 + (int(x) > h) for x in entrada[2:])

    print(ancho_total)


if __name__ == '__main__':
    solve()