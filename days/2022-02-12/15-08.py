""" https://inf-ege.sdamgia.ru/problem?id=7675
Элементами множества А являются натуральные числа. Известно, что выражение
(x ∈ {2, 4, 6, 8, 10, 12}) → (((x ∈ {3, 6, 9, 12, 15}) ∧ ¬(x ∈ A)) → ¬(x ∈ {2, 4, 6, 8, 10, 12}))
истинно при любом значении переменной х. 
Определите наименьшее возможное значение суммы элементов множества A"""

from itertools import combinations


def f(x, a):
    # global p
    f1 = x in p
    f2 = x in q
    f3 = not(x in a)
    return f1 <= ((f2 and f3) <= (not f1))


p = {2, 4, 6, 8, 10, 12}
q = {3, 6, 9, 12, 15}
r = p & q

subsets = []  # список всех подмножеств из r
for count in range(len(r)+1):
    for combo in combinations(r, count):
        subsets.append(combo)

sm = 10**9
for subset in subsets:
    if all(f(x, subset) for x in r):
        sm = min(sm, sum(subset))

print(sm)
