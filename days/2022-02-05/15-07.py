# https://inf-ege.sdamgia.ru/problem?id=7763

d, s = .0, .2

a1 = 4.0
while a1 < 31:
    a1 += s

    a2 = a1 + 0.2
    while a2 < 31:
        a2 += s

        x = 4.0
        while x < 31.0:
            x += s

            f1 = (5<=x<=30) == (14<=x<=23)
            f2 = not (a1<=x<=a2)
            f = f1 <= f2
            if not f:
                break
        else:
            d = max(d , a2-a1)

print(round(d,2))
