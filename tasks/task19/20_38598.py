# https://inf-ege.sdamgia.ru/problem?id=38598

def f20(k, p):
    if p==3:
        return k>=29
    if p in [1,2] and k>=29:
        return False
    p += 1
    b1 = f20(k+1, p)
    b2 = f20(k*2, p)
    if p==3 or p==1:
        return b1 or b2
    if p==2:
        return b1 and b2


for s in range(1, 29):
    print(s, f20(s, 0))
