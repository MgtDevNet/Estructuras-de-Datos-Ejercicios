import sys

def solve():
    entrada = set(sys.stdin.read().split()) #o(n)   
    print(4-len(entrada))
if __name__ == "__main__":
    solve() #o(n)

# el conjunto es una forma rápida de quedarnos con 
#los elementos únicos de un arreglo
