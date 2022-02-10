# https://inf-ege.sdamgia.ru/problem?id=7929
''' Элементами множеств А, P, Q являются натуральные числа, причём 
P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, 
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}. 
    Известно, что выражение
( (x ∈ A) → (x ∈ P) ) ∧ ( (x ∈ Q) → ¬(x ∈ A) )
истинно при любом значении переменной х. 
Определите наибольшее возможное количество элементов в множестве A.'''

from functools import reduce

p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
z = p.union(q)

lst = reduce(lambda P, x: P + [subset | {x} for subset in P], z, [set()])

count = 0
for a in lst:
    for x in z:
        f1 = (x in a) <= (x in p)
        f2 = (x in q) <= (not(x in a))
        f = f1 and f2
        if not f:
            break
    else:
        count = max(count,len(a))

print(count)
