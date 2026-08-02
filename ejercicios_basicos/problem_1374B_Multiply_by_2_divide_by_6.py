import sys

def solve():
    entrada = sys.stdin.read().split()
    t = int(entrada[0])
    
    for _ in range(t):
        
        resultado = []
        n = int(entrada[_+1])
        print(f"n: {n}")
        if n == 1:
            resultado.append(0)
        else:
            # 6 = 3x2, entonces  para que esto
            #sea posbile la cantidad de 3 y de dos 
            #que componen el número deber ser igual,
            #y obvio diferente de cero
            aux2 = n
            aux3 = n
            c2 = 0
            c3 = 0

            pasos = 0

            #cuantos dd
            while aux2 % 2 == 0:
                aux2 //= 2
                c2 += 1
            while aux3 % 3 == 0:
                aux3 //= 3
                c3 += 1
            print(f"c2: {c2}, c3: {c3}")
            if (c2 ==0 and c3==0) or (c2 > c3):
                resultado.append(-1)
            elif(c3 > c2):
                n = n * (2 ** (c3 - c2))
                print(f"n: {n}")
                while(n % 6 == 0):
                    n //= 6
                    pasos += 1
                if n != 1:
                    resultado.append(-1)
                else:
                    resultado.append(pasos + (c3 - c2) )
            else:
                while(n % 6 == 0):
                    n //= 6
                    pasos += 1
                if n != 1:
                    resultado.append(-1)
                else:
                    resultado.append(pasos)
        print("".join(map(str, resultado)))
        print("--------------------")

if __name__ == "__main__":
    solve()