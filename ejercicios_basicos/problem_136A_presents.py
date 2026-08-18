import sys

def solve():
    entrada = sys.stdin.read().split() #o(n)
    n = int(entrada[0]) #o(1)
    l = entrada[1:] #o(n)
    l2 = [None]*n #o(n)

    for _ in range(n): #o(n)
        i = int(l[_])-1 #índice #o(1)
        v = int(_)+1 #valor #o(1)
        l2[i] = v #o(1)
    print(" ".join(list(map(str,l2)))) #o(n)
    
if __name__ == '__main__':
    solve() #o(n)