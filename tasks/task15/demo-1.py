""" На числовой прямой даны два отрезка:
    D = [17; 58] и C = [29; 80]
Укажите наименьшую возможную длину такого отрезка A,
для которого логическое выражение
    (x ∈ D) → ((¬(x ∈ C) /\ ¬(x ∈ A)) → ¬(x ∈ D))
истинно при любом значении переменной х """


def in_set(x, lt, rt):
    return lt <= x <= rt


def f(x, lt, rt):
    f1 = in_set(x, 17, 58)
    f2 = (not in_set(x, 29, 80)) and (not in_set(x, lt, rt))
    f3 = not f1
    return f1 <= (f2 <= f3)


d = 999999
lt = 16
step = .15

while lt < 81:
    lt += step

    rt = lt + step
    while rt < 81:
        rt += step

        x = 16
        while x < 81:
            x += step

            if not f(x, lt, rt):
                break
        else:
            d = min(d, rt - lt)

print(f"{d:.2f}")
