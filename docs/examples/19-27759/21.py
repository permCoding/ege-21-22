# https://inf-ege.sdamgia.ru/problem?id=27761 10
# (a+1 and b+2) or (a*2 or b*2) | a+b>=41 | (8,s) | 1<=s<=32
'''Найдите минимальное значение S, при кот вып-ся два условия:
— у Вани есть выигрышная стратегия, позволяющая ему 
выиграть первым или вторым ходом при любой игре Пети;
— у Вани нет стратегии, которая позволит ему 
гарантированно выиграть первым ходом.'''
def f21(a, b, p):
    if p==4: return a+b>=41
    if a+b>=41: return p==2
    # if p==2 and a+b>=41: return True
    # if (p==1 or p==3) and a+b>=41: return False
    p += 1
    b1 = f21(a+1,b+2,p)
    b2 = f21(a+2,b+1,p)
    b3 = f21(a*2,b,p)
    b4 = f21(a,b*2,p)
    if p==1 or p==3:
        return b1 and b2 and b3 and b4
    return b1 or b2 or b3 or b4

# for s in range(1, 33):
#     if f21(8, s, 0):
#         print(s)

# = = = = = = = = = = = = = = = = 

def f21_(a, b, p):
    if p==2: return a+b>=41
    if p==1 and a+b>=41: return False
    p += 1
    b1 = f21_(a+1,b+2,p)
    b2 = f21_(a+2,b+1,p)
    b3 = f21_(a*2,b,p)
    b4 = f21_(a,b*2,p)
    if p==1:
        return b1 and b2 and b3 and b4
    return b1 or b2 or b3 or b4

for s in range(1, 33):
    if f21_(8, s, 0):
        print(s)  # 15 16