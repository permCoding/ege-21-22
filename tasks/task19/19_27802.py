# https://inf-ege.sdamgia.ru/problem?id=27802
""" +1 or +4 or *5 || >=68 || 1 (S) 67 """

def f19(a,p):
    if p==2:
        return a>=68
    p +=1
    b1 = f19(a+1,p)
    b2 = f19(a+4,p)
    b3 = f19(a*5,p)    
    return b1 or b2 or b3


for s in range(1, 68):
    if f19(s,0):
        print(s)
        break
