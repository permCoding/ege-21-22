# https://inf-ege.sdamgia.ru/problem?id=7763

def check(x, a1, a2):
    f1 = 5 <= x <= 30
    f2 = 14 <= x <= 23
    f3 = not (a1 <= x <= a2)
    return (f1 == f2) <= f3


d = 80 - 17

a1 = 4
while a1 <= 31:
    a1 += 0.1
    a2 = a1
    while a2 <= 31:
        a2 += 0.1
        b = True
        x = 4
        while x <= 31:
            x += .1
            if not check(x, a1, a2):
                b = False
                break
        if b:
            d = max(a2 - a1, d)

print(round(d, 0))
