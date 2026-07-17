# A. Puzzles
# time limit per test1 second
# memory limit per test256 megabytes
# The end of the school year is near and Ms. Manana, the teacher, will soon have to say goodbye to a yet another class. She decided to prepare a goodbye present for her n students and give each of them a jigsaw puzzle (which, as wikipedia states, is a tiling puzzle that requires the assembly of numerous small, often oddly shaped, interlocking and tessellating pieces).

# The shop assistant told the teacher that there are m puzzles in the shop, but they might differ in difficulty and size. Specifically, the first jigsaw puzzle consists of f1 pieces, the second one consists of f2 pieces and so on.

# Ms. Manana doesn't want to upset the children, so she decided that the difference between the numbers of pieces in her presents must be as small as possible. Let A be the number of pieces in the largest puzzle that the teacher buys and B be the number of pieces in the smallest such puzzle. She wants to choose such n puzzles that A - B is minimum possible. Help the teacher and find the least possible value of A - B.

# Input
# The first line contains space-separated integers n and m (2 ≤ n ≤ m ≤ 50). The second line contains m space-separated integers f1, f2, ..., fm (4 ≤ fi ≤ 1000) — the quantities of pieces in the puzzles sold in the shop.

# Output
# Print a single integer — the least possible difference the teacher can obtain.


import sys

n,m = map(int, sys.stdin.readline().split()) #o(1)
l = list(map(int, sys.stdin.readline().split())) #o(m)
l.sort() #o(mlog(m)), es una buena idea
r = None
if m > n: #o(1)
    for i in range(m): #o(m)
        if l.count(l[i])==n: #o(m)      } o(m^2) #esto se puede mejorar
            r = 0
            break
    
    if r == None:
        c = 0
        dif =[]
        for j in range(m-n+1): #o(m)
            l1 = l[c:c+n] #o(n)                         } o(m*n)
            dif.append(max(l1)-min(l1)) #o(n)   #tal vez esto se pueda mejorar.
            c+=1 
        r = min(dif)
else:
    r = l[-1]-l[0]
print(r)

#complejidad final -> 1 + m + mlog(m) + m^2 + m*n -> o(m^2)

#recordemos que nos queadmos con la complejidad que crezca más rápido, por tanto
# aunque se solucione el problema, la complejidad es bastante mala.  

