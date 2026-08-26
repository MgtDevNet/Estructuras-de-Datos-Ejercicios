import sys

def solve():
    entrada = iter(sys.stdin.read().split()) #o(n)
    n = int(next(entrada)) #o(1)
    p = list(next(entrada).lower()) #o(n)

    if n < 26: #o(1)
        print("NO") #o(1)
    else:
        #los volvemos únicos
        p_conjunto = set(p) #o(n)
        if len(p_conjunto)<26: #o(1)
            print("NO") #o(1)
        else:
            #la única opción de que sean únicos
            # y que sean 26 es que sean todos los
            #valores del alfabeto
            print("YES") #o(1)
if __name__ == '__main__':
    solve() #o(n)