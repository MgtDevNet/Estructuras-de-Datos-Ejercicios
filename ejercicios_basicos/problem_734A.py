import sys

def solve():
    entrada = iter(sys.stdin.read().split())
    n = int(next(entrada))
    s = list(next(entrada))
    a = s.count("A")
    d = s.count("D")
    if a > d:
        print("Anton")
    elif a<d:
        print("Danik")
    else:
        print("Friendship")
if __name__ == '__main__':
    solve()