import sys

def solve():
    entrada = iter(sys.stdin.read().split())
    n = int(next(entrada))
    c = 0
    for _ in range(n):
        q = int(next(entrada))
        p = int(next(entrada))
        print("-")
        print(f"p:{p} q{q}")
        if q <= p-2:
            c+=1
    print(c) 

if __name__ == '__main__':
    solve()