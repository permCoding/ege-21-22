# https://inf-ege.sdamgia.ru/problem?id=27759 9
# (a+1 and b+2) or (a*2 or b*2) | a+b>=41 | (8,s) | 1<=s<=32
'''Ваня выиграл своим первым ходом после неудачного первого хода Пети
Укажите минимальное значение S, когда такая ситуация возможна'''
def f19(a, b, p):
    if p==2: return a+b>=41
    # if p==1 and a+b>=41: return False
    p += 1
    b1 = f19(a+1,b+2,p)
    b2 = f19(a+2,b+1,p)
    b3 = f19(a*2,b,p)
    b4 = f19(a,b*2,p)
    return b1 or b2 or b3 or b4

for s in range(1, 33):
    if f19(8, s, 0):
        print(s)
        break
