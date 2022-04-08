# https://inf-ege.sdamgia.ru/problem?id=27416
""" +1 *2 || >=77 || (7,S) """

def f19(a,b,p):
    if p==2:
        return a+b>=77
    p +=1
    b1 = f19(a+1,b,p)
    b2 = f19(a*2,b,p)
    b3 = f19(a,b+1,p)
    b4 = f19(a,b*2,p)
    return b1 or b2 or b3 or b4


for s in range(1, 70):
    if f19(7,s,0):
        print(s)
        break
