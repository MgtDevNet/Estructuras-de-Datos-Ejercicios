import sys

import sys

def solve():
    linea = sys.stdin.readline().strip()
    if not linea:
        return
    x = int(linea)
    
    # .bit_count() cuenta cuántos '1's tiene el número en binario
    print(x.bit_count())

if __name__ == '__main__':
    solve()