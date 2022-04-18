# https://inf-ege.sdamgia.ru/problem?id=27748 16 19
# +1 *4 || >=82 || (4,S) 1<=S<=77 """
"""Найдите два таких значения S, при которых у Пети есть
   выигрышная стратегия, причём одновр выполняются два условия:
— Петя не может выиграть за один ход;
— Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня."""
def f20(a, b, p):
    if p==3: return a+b>=82
    if (p==1 or p==2) and a+b>=82: return False
    p +=1
    b1 = f20(a+1,b,p)
    b2 = f20(a*4,b,p)
    b3 = f20(a,b+1,p)
    b4 = f20(a,b*4,p)
    if p==2:
        return b1 and b2 and b3 and b4
    return b1 or b2 or b3 or b4


for s in range(1, 78):
    if f20(4, s, 0):
        print(s)
