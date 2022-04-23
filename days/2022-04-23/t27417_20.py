# https://inf-ege.sdamgia.ru/problem?id=27417
# +1 *2 | k>=77 | 1 <= S <= 69 | (7,s)
"""Найдите два таких значения S, при которых у Пети
есть выигрышная стратегия, причём одновременно выполняются два условия:
— Петя не может выиграть за один ход;
— Петя может выиграть своим вторым ходом независимо 
от того, как будет ходить Ваня."""
# 0 1 2 3 4
# 0 П В П В
def f20(a,b,p):
    if p==3: return a+b>=77
    if p<3 and a+b>=77: return False
    p += 1
    b1, b2 = f20(a+1,b,p), f20(a,b+1,p)
    b3, b4 = f20(a*2,b,p), f20(a,b*2,p)
    if p==2: return b1 and b2 and b3 and b4
    return b1 or b2 or b3 or b4

for s in range(1, 70):
    if f20(7,s,0):
        print(s)
