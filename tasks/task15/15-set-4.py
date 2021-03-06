# https://inf-ege.sdamgia.ru/problem?id=9202
''' Элементами множеств А, P, Q являются натуральные числа, причём 
P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, 
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}. 
    Известно, что выражение
((x ∈ A) → (x ∈ P)) V (¬(x ∈ Q) → ¬(x ∈ A))
истинно при любом значении переменной х. 
Определите наибольшее возможное количество элементов в множестве A.'''

from itertools import combinations

p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
z = p.union(q)

subsets = []
for i in range(len(z)+1):
    for combo in combinations(z,i):
        subsets.append(set(combo))

d = 0  # будем искать наибольшее
for a in subsets:
    for x in z:
        f1 = (x in a) <= (x in p)
        f2 = (x not in q) <= (x not in a)
        f = f1 or f2
        if not f:
            break
    else:
        d = max(d,len(a))
        # if len(a) == 3:
        #     print(a)

print(d)

# +++