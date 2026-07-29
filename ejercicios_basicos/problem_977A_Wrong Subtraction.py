import sys

def solve():
    entrada = sys.stdin.read().split()
    n = entrada[0]
    k = int(entrada[1])
    
    for i in range(k):
        if n[-1] == "0":
            n = int(float(n))//10
        else:
            n = int(float(n))-1
        n = str(n)
        #print(i,n)
    print(n)

if __name__ == '__main__':
    solve()