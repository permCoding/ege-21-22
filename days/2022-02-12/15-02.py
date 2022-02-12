""" На числовой прямой даны два отрезка:
    D = [17; 58] и C = [29; 80]
Укажите наименьшую возможную длину такого отрезка A,
для которого логическое выражение
    (x ∈ D) → ((¬(x ∈ C) /\ ¬(x ∈ A)) → ¬(x ∈ D))
истинно при любом значении переменной х """

from time import monotonic

def f(x, lt, rt):
    f1 = 17 <= x <= 58
    f2 = not (29 <= x <= 80) and not (lt <= x <= rt)
    return f1 <= (f2 <= (not f1))


start = monotonic()

st = 0.1
d = 9999999
lt = 16
while lt < 81:
    lt += st
    rt = lt + st
    while rt < 81:
        rt += st
        x = 16
        while x < 81:
            x += st
            if not f(x, lt, rt):
                break
        else:
            d = min(d, rt - lt)
print(round(d, 2))

finish = monotonic()
result = finish - start
print(round(result, 2))
