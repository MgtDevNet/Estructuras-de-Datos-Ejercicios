import sys

def solve():
    entrada = iter(sys.stdin.read().split()) #o(n)
    n = int(next(entrada))#o(1)
    c = 0 #o(1)
    maximo = c #o(1)
    #print(entrada)
    for _ in range(n): #o(n)
        a = int(next(entrada)) #o(1)
        b = int(next(entrada)) #o(1)
        c -= a #o(1)
        c += b #o(1)
        if maximo < c: #o(1)
            maximo = c #o(1)
    print(maximo) #o(1)


if __name__ == "__main__":
    solve()

#complejidad final es o(n)