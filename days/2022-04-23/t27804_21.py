# https://inf-ege.sdamgia.ru/problem?id=27804
# +1 +4 *5 | k>=68 | 1<=S<=67 | (s)
"""Найдите минимальное значение S, при котором одновременно 
выполняются два условия:
— у Вани есть выигрышная стратегия, позволяющая ему 
выиграть первым или вторым ходом при любой игре Пети;
— у Вани нет стратегии, которая позволит ему 
гарантированно выиграть первым ходом."""
# 0 1 2 3 4
# 0 П В П В
def f21(k,p):
    if p==4: return k>=68
    if p==2 and k>=68: return True
    if (p==1 or p==3) and k>=68: return False
    p += 1
    b1 = f21(k+1,p)
    b2 = f21(k+4,p)
    b3 = f21(k*5,p)
    if p==1 or p==3: return b1 and b2 and b3
    return b1 or b2 or b3

for s in range(1, 68):  # 8 11 13
    if f21(s,0):
        print(s)

# = = = = = = = = 
"""у Вани есть страт, которая позволит ему 
гарантированно выиграть первым ходом."""
def f21_(k,p):
    if p==2: return k>=68
    if p==1 and k>=68: return False
    p += 1
    b1 = f21_(k+1,p)
    b2 = f21_(k+4,p)
    b3 = f21_(k*5,p)
    if p==2: return b1 or b2 or b3
    if p==1: return b1 and b2 and b3

for s in range(1, 68):
    if f21_(s,0):
        print(s)