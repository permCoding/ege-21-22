# https://inf-ege.sdamgia.ru/problem?id=27747
# +1 *4 || >=82 || (4,S) 1<=S<=77
""" Ваня выиграл своим первым ходом после неудачного первого хода Пети
Укажите минимальное значение S, когда такая ситуация возможна"""


def f19(a, b, p):
    if p == 2:
        return a + b >= 82
    p += 1
    b1 = f19(a + 1, b, p)
    b2 = f19(a * 4, b, p)
    b3 = f19(a, b + 1, p)
    b4 = f19(a, b * 4, p)
    return b1 or b2 or b3 or b4


for s in range(1, 78):
    if f19(4, s, 0):
        print(s)
        break
