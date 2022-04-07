# https://inf-ege.sdamgia.ru/problem?id=36874

def f20(a, b, p):
    if p==3:
        return a+b>=88
    else:
        if a+b>=88:
            return False
    p += 1
    b1 = f20(a+1,b,p)
    b2 = f20(a,b+1,p)
    b3 = f20(a*3,b,p)
    b4 = f20(a,b*3,p)
    if p==2:
        return b1 and b2 and b3 and b4
    return b1 or b2 or b3 or b4


for s in range(1, 101):
    if f20(6,s,0):
        print(s)

"""
0 1 2 3 4 5
= П В П В
"""