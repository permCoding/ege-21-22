# https://inf-ege.sdamgia.ru/problem?id=36874 10

def f19(a, b, p):
    if p == 2: return a+b >= 88
    p += 1
    b1 = f19(a+1, b, p)
    b2 = f19(a, b+1, p)
    b3 = f19(a*3, b, p)
    b4 = f19(a, b*3, p)
    return b1 or b2 or b3 or b4


for s in range(1, 72):
    if f19(6, s, 0):
        print(s)
        break
