import sys

def solve():
    entrada = iter(sys.stdin.read().split()) #o(n)
    l1 = next(entrada)
    l2 = next(entrada)
    respuesta = []
    for a,b in zip(l1,l2):
        if a == b:
            respuesta.append("0")#o(1)
        else:
            respuesta.append("1")#o(1)
    print("".join(respuesta)) #o(n)
if __name__ == '__main__':
    solve() #o(n)

# sin embargo, estre problema pide aplicar la operación XOR binaria
# bit a bit: si los caracteres son iguales, siempre imprime 0, y si son diferentes
# imprime 1.
# import sys


# def solve():
#     entrada = sys.stdin.read().split()
#     if not entrada:
#         return

#     l1, l2 = entrada[0], entrada[1]

#     # '1' si los caracteres son distintos, '0' si son iguales
#     ans = ''.join('1' if a != b else '0' for a, b in zip(l1, l2))

#     print(ans)


# if __name__ == '__main__':
#     solve()
