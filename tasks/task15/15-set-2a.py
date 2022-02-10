# https://inf-ege.sdamgia.ru/problem?id=7675
''' Элементами множеств А, P, Q являются натуральные числа, причём 
    Известно, что выражение
(x ∈ {2, 4, 6, 8, 10, 12}) → (((x ∈ {3, 6, 9, 12, 15}) ∧ ¬(x ∈ A)) → ¬(x ∈ {2, 4, 6, 8, 10, 12}))
истинно при любом значении переменной х. 
Определите наименьшее возможное значение суммы элементов множества A.'''

from itertools import combinations

p = {2, 4, 6, 8, 10, 12}
q = {3, 6, 9, 12, 15}
z = p.union(q)

subsets = []
for i in range(len(z)+1):
    for combo in combinations(z,i):
        subsets.append(set(combo))

sm = 999999  # будем искать наименьшее
for a in subsets:
    for x in z:
        f = (x in p) <= (((x in q) and (x not in a)) <= (x not in p))
        if not f:
            break
    else:
        sm = min(sm,sum(a))

print(sm)

# +++