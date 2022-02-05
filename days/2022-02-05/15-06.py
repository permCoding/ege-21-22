# https://inf-ege.sdamgia.ru/problem?id=7763
# решение в целых числах не гарантирует правильный ответ
d = 0
for a1 in range(4, 32):
    for a2 in range(a1+1, 32):
        for x in range(4, 32):
            f1 = ((5<=x<=30) == (14<=x<=23))
            f2 = not (a1<=x<=a2)
            f = f1 <= f2
            if f == False:
                break
        else:
            d = max(d, a2-a1)

print(d)  # тут ответ неверный
