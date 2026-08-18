import sys

def solve():
    entrada = sys.stdin.read().split() #o(n)
    n = int(entrada[0]) #o(1)
    c = 0 #o(1)
    for _ in range(1,n): #o(n)
        l1 = list(entrada[_]) #o(1)
        l2 = list(entrada[_+1]) #o(1)
        a = l1[1] #o(1)
        b = l2[0]#o(1)
        #print(f"l1{l1}")
        #print(f"l2{l2}")
        #print(f"a {a} b {b}")

        if a == b : #o(1)
            c+=1 #o(1)
        
    print(c+1)


if __name__ == '__main__':
    solve() #o(n)
