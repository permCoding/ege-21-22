# https://inf-ege.sdamgia.ru/problem?id=36874

def f19(a, b, p):
    if p==2:
        return a+b>=88
    p += 1
    return \
        f19(a+1,b,p) or \
        f19(a,b+1,p) or \
        f19(a*3,b,p) or \
        f19(a,b*3,p)


for s in range(1, 101):
    if f19(6,s,0):
        print(s)
        break
