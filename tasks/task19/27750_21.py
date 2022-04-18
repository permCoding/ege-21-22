# https://inf-ege.sdamgia.ru/problem?id=27750 18
# +1 *4 || >=82 || (4,S) 1<=S<=77 """
"""Найдите минимальное значение S, при котором одновременно выполняются два условия:
— у Вани есть выигрышная стратегия, позволяющая ему
  выиграть первым или вторым ходом при любой игре Пети;
— у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом."""
def f21(a, b, p):
    if p==4: return a+b>=82
    if p==2 and a+b>=82: return True
    if (p==1 or p==3) and a+b>=82: return False
    p +=1
    b1 = f21(a+1,b,p)
    b2 = f21(a*4,b,p)
    b3 = f21(a,b+1,p)
    b4 = f21(a,b*4,p)
    if p==1 or p==3:
        return b1 and b2 and b3 and b4
    return b1 or b2 or b3 or b4


for s in range(1, 78):
    if f21(4, s, 0):
        print(s)

# = = = = = = = = = = = = = = =
# def f21(a, b, p):
#     if p==2: return a+b>=82
#     if p==1 and a+b>=82: return False
#     p +=1
#     b1 = f21(a+1,b,p)
#     b2 = f21(a*4,b,p)
#     b3 = f21(a,b+1,p)
#     b4 = f21(a,b*4,p)
#     if p==2:
#         return b1 or b2 or b3 or b4
#     return b1 and b2 and b3 and b4
#
# for s in range(1, 78):
#     if f21(4, s, 0):
#         print(s)
