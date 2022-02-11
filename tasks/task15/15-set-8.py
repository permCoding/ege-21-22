""" 
Элементами множеств А, P, Q являются натуральные числа, причём 
    P = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21} 
    Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
Известно, что выражение
    ((x ∈ P) → (x ∈ A)) V (¬(x ∈ A) → ¬(x ∈ Q))
истинно при любом значении переменной х. 
Определите наименьшее возможное значение суммы элементов множества A """

def get_subsets(pos):
    if pos == 0:
        subsets.append(subset[:])
    else:
        subset.append(r[pos-1])
        get_subsets(pos-1)
        subset.pop()
        get_subsets(pos-1)


subsets = []
subset = []

p = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
r = list(p.union(q))

get_subsets(len(r))

def f(x, a):
    return ((x in p) <= (x in a)) or ((x not in a) <= (x not in q))


sm = 999999
for subset in subsets:
    lst = [f(x, subset) for x in r]
    if all(lst):
        sm = min(sm, sum(subset))
print(sm)

