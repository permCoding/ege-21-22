# https://inf-ege.sdamgia.ru/problem?id=38597

def f19(k, p):
    if p==2:
        return k>=29
    if p==1 and k>=29:
        return False
    p += 1
    b1 = f19(k+1, p)
    b2 = f19(k*2, p)
    if p==2:
        return b1 or b2
    if p==1:
        return b1 and b2


for s in range(1, 29):
    print(s, f19(s, 0))
