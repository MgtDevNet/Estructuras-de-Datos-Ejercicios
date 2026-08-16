import sys

def solve():
    n = int(sys.stdin.readline().strip())
    if n & 1 == 0: # verificar paridad
        print(n//2)
    else:
        print(-(n+1)//2)
if __name__ == '__main__':
    solve() #o(1)