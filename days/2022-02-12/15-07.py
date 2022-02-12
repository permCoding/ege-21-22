""" https://inf-ege.sdamgia.ru/problem?id=7929
Элементами множеств А, P, Q являются натуральные числа, причём 
    P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20} 
    Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
Известно, что выражение
    ( (x ∈ A) → (x ∈ P) ) ∧ ( (x ∈ Q) → ¬(x ∈ A) )
истинно при любом значении переменной х. 
Определите наибольшее возможное количество элементов в множестве A"""

from itertools import combinations


def f(x, a):
    f1 = (x in a) <= (x in p)
    f2 = (x in q) <= (x not in a)
    return f1 and f2


p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20} 
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
r = p.union(q)

subsets = []  # список всех подмножеств из r
for count in range(len(r)+1):
    for combo in combinations(r, count):
        subsets.append(combo)

count = 0
for subset in subsets:
    if all(f(x, subset) for x in r):
        count = max(count, len(subset))
print(count)

# это решение
