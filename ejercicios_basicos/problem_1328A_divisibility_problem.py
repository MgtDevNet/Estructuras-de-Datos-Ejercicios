import sys

def solve():
    entrada = iter(sys.stdin.read().split())
    t = int(next(entrada))
    for _ in range(t):
        a,b = int(next(entrada)),int(next(entrada))
        if a % b == 0:
            print(0)
        else:
            if a > b:
                aux = (a // b) + 1
            else:
                aux = 1 
            print((b * aux) - a)

if __name__ == "__main__":
    solve()