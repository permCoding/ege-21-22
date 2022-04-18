# https://inf-ege.sdamgia.ru/problem?id=36875 27
"""Найдите максимальное значение S, при котором у Вани есть выигрышная
стратегия, позволяющая ему выиграть при любой игре Пети."""
def f21(a, b, p):
    if p==4: return a+b>=88
    if p==2 and a+b>=88: return True
    if a+b>=88: return False
    p += 1
    b1 = f21(a+1, b, p)
    b2 = f21(a, b+1, p)
    b3 = f21(a*3, b, p)
    b4 = f21(a, b*3, p)
    if p==1 or p==3:
        return b1 and b2 and b3 and b4
    return b1 or b2 or b3 or b4


for s in range(1, 78):
    if f21(6, s, 0):
        print(s)

"""
0 1 2 3 4 5
= П В П В
"""
