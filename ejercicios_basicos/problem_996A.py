import sys
 
def solve():
    n = int(sys.stdin.readline().strip())
    v = [100,20,10,5,1]
    
    c = 0
    for _ in v:
        if n >= _ :
            aux = n // _
            c += aux
            n -= (aux * _)
        #print(n)
    print(c)
        
 
 
 
if __name__ == '__main__':
    solve()