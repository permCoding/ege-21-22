# https://inf-ege.sdamgia.ru/problem?id=13467
''' Элементами множеств А, P, Q являются натуральные числа, причём 
P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, 
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}. 
    Известно, что выражение
((x ∈ P) → (x ∈ A)) V (¬(x ∈ A) → ¬(x ∈ Q))
истинно при любом значении переменной х. 
Определите наименьшее возможное значение суммы элементов множества A.'''

from itertools import combinations

p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
z = p.union(q)

subsets = []
for i in range(len(z)+1):
    for combo in combinations(z,i):
        subsets.append(set(combo))

d = 999999  # будем искать наименьшее
for a in subsets:
    for x in z:
        f1 = (x in p) <= (x in a)
        f2 = (x not in a) <= (x not in q)
        f = f1 or f2
        if not f:
            break
    else:
        d = min(d,len(a))
        # if len(a) == 3:
        #     print(a)
        #     print(sum(a))

print(d)

# +++