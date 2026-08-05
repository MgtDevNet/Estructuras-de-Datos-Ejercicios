import sys

def solve():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    
    t = int(entrada[0])
    idx = 1
    respuestas = []
    
    for _ in range(t):
        n = int(entrada[idx])
        k = int(entrada[idx + 1])
        idx += 2
        
        # Fórmula limpia O(1)
        ans = k + (k - 1) // (n - 1)
        respuestas.append(str(ans))
        
    sys.stdout.write("\n".join(respuestas) + "\n")

if __name__ == '__main__':
    solve()