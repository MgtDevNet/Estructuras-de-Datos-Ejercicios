import sys
import bisect


def solve():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    n = int(entrada[0])
    x = list(map(int, entrada[1 : n + 1]))
    x.sort()  # O(n log n)
    q = int(entrada[n + 1])

    respuestas = []
    indice = n + 2

    for _ in range(q):
        m = int(entrada[indice])
        indice += 1

        # bisect_right nos da directamente la cantidad de precios <= m
        cant_tiendas = bisect.bisect_right(x, m)
        respuestas.append(str(cant_tiendas))

    sys.stdout.write('\n'.join(respuestas) + '\n')


if __name__ == '__main__':
    solve()

# 5
# 3 10 8 6 11
# 4
# 1
# 10
# 3
# 11