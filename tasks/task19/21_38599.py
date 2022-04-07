# https://inf-ege.sdamgia.ru/problem?id=38599

def f21(k, p):
    if p==4:
        return k>=29
    if k>=29:
        return p==2
    p += 1
    b1 = f21(k+1, p)
    b2 = f21(k*2, p)
    if p==4 or p==2:
        return b1 or b2
    if p==3 or p==1:
        return b1 and b2

for s in range(1, 29):
    print(s, f21(s, 0))

print()

def f21_(k, p):
    if p==2:
        return k>=29
    if k>=29:  # p==1
        return False
    p += 1
    b1 = f21_(k+1, p)
    b2 = f21_(k*2, p)
    if p==2:
        return b1 or b2
    if p==1:
        return b1 and b2

for s in range(1, 29):
    print(s, f21_(s, 0))
""" найдите значение S, при котором одновременно выполняются два условия:
— у Вани есть выигрышная стратегия, позволяющая ему выиграть 
  первым или вторым ходом при любой игре Пети;
— у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
Если найдено несколько значений S, в ответе запишите минимальное из них."""