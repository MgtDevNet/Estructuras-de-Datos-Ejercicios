import sys

def solve():
    x = int(sys.stdin.readline().strip())

    #Si es una potencia exacta de 2, entonces
    #solo basta con 1 bacteria y posteriormente se llegará
    #a ese resultado

    if x & (x-1) == 0:
        print(1)
    else:
        dif = 1
        for i in range(1,x):
            aux = 2**i
            if aux > x:
                dif = x - 2**(i-1)
                break
        print(1+(dif))

if __name__ == '__main__':
    solve()