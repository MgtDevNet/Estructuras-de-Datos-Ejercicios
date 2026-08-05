import sys

def solve():
    n = sys.stdin.readline().strip() #o(1)
    if n == "9": #o(1)
        n_nuevo2=n #o(1) 
    elif len(n) == 1 and int(n)>=5: #o(1)
            n_nuevo2=9-int(n) #o(1)
    elif len(n) == 1 and int(n)<5: #o(1)
        n_nuevo2 = n #o(1)
    else: 
        minimo = int(n) #o(1)
        n_nuevo = n #o(1)
        n_conjunto =list(set(n)) #o(n)
        #print(len(n_conjunto))
        for i in range(len(n_conjunto)): #o(m) siendo m el número de valores único
            #print(n[i],int(n[i])>=5)
            if int(n_conjunto[i])>=5: #o(1)
                n_nuevo=n_nuevo.replace(n_conjunto[i],str(9-int(n_conjunto[i]))) #o(n) debe recorrer todo 
        #CICLO FOR O(M*N) PERO M SON 10 DÍGITOS MÁXIMOS, ENTONCES O(N)
        if minimo < int(n_nuevo): #o(1)
            n_nuevo2 = minimo #o(1)
        else: #o(1)
            n_nuevo2 = n_nuevo #o(1)

        if n[0] == "9": #o(1)
            n_nuevo2 = "9"+ n_nuevo[1:] #o(1)
        
    print(n_nuevo2)
if __name__ == "__main__":
    solve()

#la complejidad final sería o(n+m) -> o(n)