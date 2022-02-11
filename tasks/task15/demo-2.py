""" На числовой прямой даны два отрезка:
    D = [17; 58] и C = [29; 80]
Укажите наименьшую возможную длину такого отрезка A,
для которого логическое выражение
    (x ∈ D) → ((¬(x ∈ C) /\ ¬(x ∈ A)) → ¬(x ∈ D))
истинно при любом значении переменной х """


def f(x, lt, rt):
    f1 = 17 <= x <= 58
    f2 = not(29 <= x <= 80) and not(lt <= x <= rt)
    return f1 <= (f2 <= (not f1))


st = 3
d = 999999
for lt in range(160, 810, st):
    for rt in range(lt+st, 810, st):
        lst = [f(x/10, lt/10, rt/10) for x in range(160, 810, st)]
        if all(lst):
            d = min(d, rt-lt)
print(f"{d/10:.2f}")
