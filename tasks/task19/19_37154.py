# https://inf-ege.sdamgia.ru/problem?id=37154
""" +1 or +4 or *2 || Win>=40 || 1<=S<=39 """

def f19(a,p):
    if p==2:
        return a>=40
    if p==1 and a>=40: return False
    p +=1
    b1 = f19(a+1,p)
    b2 = f19(a+4,p)
    b3 = f19(a*2,p)
    if p==1:  
        return b1 and b2 and b3  # любой ход Пети
    return b1 or b2 or b3  # Ваня может выиграть


for s in range(1, 40):
    print(s, f19(s, 0))
