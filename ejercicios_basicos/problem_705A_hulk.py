import sys

def solve():

    n = int(sys.stdin.readline().strip()) #o(1)
    respuesta = "" #o(1)
    for i in range(1,n+1): #o(n)
        if i>1:
            respuesta += " that "
        if i & 1 != 0:
            respuesta += "I hate"
        else:
            respuesta += "I love"
        
    respuesta += " it"
    print(respuesta)

if __name__ == '__main__':
    solve() #o(n)