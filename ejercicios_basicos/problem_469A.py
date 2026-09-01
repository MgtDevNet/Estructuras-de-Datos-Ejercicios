import sys
 
def solve():
    entrada = sys.stdin.read().split()
    n = int(entrada[0])
    p = int(entrada[1])
    x = entrada[2:2+p]
    y = entrada[2+p+1:]
    z = set(x+y)
 
    if len(z) == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
    
 
 
if __name__ == '__main__':
    solve()