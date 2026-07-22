# l = [39, 64, 93, 114, 159, 190, 226, 239, 244, 279, 525, 528, 619, 628, 643, 650, 697, 763, 763, 790, 847, 882, 884, 894, 999]
# for j in range(24,25):
#     print(j)
    
# import math
# def construir_criba(limite):
#     """
#     Genera un arreglo booleano donde es_primo[i] es True si i es primo.
#     Usa la Criba de Eratóstenes en O(N log(log N)).
#     """
#     es_primo = [True] * (limite + 1)
#     es_primo[0] = es_primo[1] = False  # 0 y 1 no son primos
    
#     for i in range(2, int(math.isqrt(limite)) + 1):
#         if es_primo[i]:
#             # Marcamos todos los múltiplos de i como no primos
#             for j in range(i * i, limite + 1, i):
#                 es_primo[j] = False
                
#     return es_primo



# print(construir_criba(6))

import numpy as np
a = set(np.array([1,2,3])-1)
print(a)


