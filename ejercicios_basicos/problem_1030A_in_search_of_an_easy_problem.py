import sys
import bisect
#la búsqueda más optima de buscar es con búsqueda binaria 

def solve():
    entrada = sys.stdin.read().split() #O(n+1)
    n = int(entrada[0]) #o(1)
    l = list(map(int,entrada[1:])) #o(n)
    l.sort() #para ordenar o(nlog(n))
    idx = bisect.bisect_left(l,1) #o(log(n))

    if idx < len(l) and l[idx] == 1: #o(1)
        print("HARD") #o(1)
    else:
        print("EASY") #o(1)
if __name__ == "__main__":
    solve() #o(nlog(n)) pues es el mayor