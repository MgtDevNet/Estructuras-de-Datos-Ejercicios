

import sys

def solve():
    n, m = map(int, sys.stdin.read().split())
    
    # Si la cantidad de turnos (min(n, m)) es impar gana Akshat, si es par gana Malvika
    if min(n, m) % 2 != 0:
        print("Akshat")
    else:
        print("Malvika")

if __name__ == '__main__':
    solve()