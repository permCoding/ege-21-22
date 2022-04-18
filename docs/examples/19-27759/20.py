# https://inf-ege.sdamgia.ru/problem?id=27760 14
# (a+1 and b+2) or (a*2 or b*2) | a+b>=41 | (8,s) | 1<=s<=32
'''Найдите максимальное S, при котором у Пети есть выигрышная 
стратегия, причём одновременно выполняются два условия:
— Петя не может выиграть за один ход;
— Петя может выиграть своим вторым ходом независимо от того, 
  как будет ходить Ваня.'''
def f20(a, b, p):
    if p==3: return a+b>=41
    if a+b>=41: return False
    p += 1
    b1 = f20(a+1,b+2,p)
    b2 = f20(a+2,b+1,p)
    b3 = f20(a*2,b,p)
    b4 = f20(a,b*2,p)
    if p==2:
        return b1 and b2 and b3 and b4
    return b1 or b2 or b3 or b4

for s in range(1, 33):
    if f20(8, s, 0):
        print(s)  # максимальное
