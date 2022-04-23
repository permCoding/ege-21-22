# https://inf-ege.sdamgia.ru/problem?id=27416
# +1 *2 | k>=77 | 1 <= S <= 69 | (7,s)
"""Ваня выиграл своим первым ходом после неудачного 
первого хода Пети. Укажите минимальное значение S, 
когда такая ситуация возможна"""
# 0 1 2 3 4
# 0 П В П В
def f19(a,b,p):
    if p==2: return a+b>=77
    # if p==1 and a+b>=77: return False
    p += 1
    b1, b2 = f19(a+1,b,p), f19(a,b+1,p)
    b3, b4 = f19(a*2,b,p), f19(a,b*2,p)
    return b1 or b2 or b3 or b4

for s in range(1, 70):
    if f19(7,s,0):
        print(s)
        break