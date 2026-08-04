import sys

def solve():
    n = sys.stdin.readline().strip()
    if n == "9":
        n_nuevo2=n
    elif len(n) == 1 and int(n)>=5:
            n_nuevo2=9-int(n)
    elif len(n) == 1 and int(n)<5:
        n_nuevo2 = n
    else:
        minimo = int(n)
        n_nuevo = n
        n_conjunto =list(set(n))
        #print(len(n_conjunto))
        for i in range(len(n_conjunto)):
            #print(n[i],int(n[i])>=5)
            if int(n_conjunto[i])>=5:
                n_nuevo=n_nuevo.replace(n_conjunto[i],str(9-int(n_conjunto[i])))

        if minimo < int(n_nuevo):
            n_nuevo2 = minimo
        else:
            n_nuevo2 = n_nuevo

        if n[0] == "9":
            n_nuevo2 = "9"+ n_nuevo[1:]
        
    print(n_nuevo2)
if __name__ == "__main__":
    solve()