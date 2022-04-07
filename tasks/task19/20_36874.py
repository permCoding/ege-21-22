# https://inf-ege.sdamgia.ru/problem?id=36874

def f20(a, b, p):
    if p==3:
        return a+b>=88
    else:
        if a+b>=88:
            return False
    p += 1
    if p==2:
        return f20(a+1,b,p) and f20(a,b+1,p) and f20(a*3,b,p) and f20(a,b*3,p)
    return f20(a+1,b,p) or \
        f20(a,b+1,p) or \
        f20(a*3,b,p) or \
        f20(a,b*3,p)


for s in range(1, 101):
    if f20(6,s,0):
        print(s)

"""
0 1 2 3 4 5
= П В П В
"""