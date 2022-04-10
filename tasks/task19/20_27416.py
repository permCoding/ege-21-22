# https://inf-ege.sdamgia.ru/problem?id=27748
""" +1 *4 || >=82 || (4,S) 1<=S<=77 """

def f20(a, b, p):
    if (p==1 or p==2) and a+b>=82: return False
    if p==3: return a+b>=82
    p +=1
    b1 = f20(a+1,b,p)
    b2 = f20(a*4,b,p)
    b3 = f20(a,b+1,p)
    b4 = f20(a,b*4,p)
    if p==3 or p==1:
        return b1 or b2 or b3 or b4
    return b1 and b2 and b3 and b4


for s in range(1, 78):
    if f20(4, s, 0):
        print(s)
