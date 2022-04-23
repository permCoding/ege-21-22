# https://inf-ege.sdamgia.ru/problem?id=27802
# +1 +4 *5 | k>=68 | 1<=S<=67 | (s)
"""Ваня выиграл своим первым ходом после неудачного 
первого хода Пети. Укажите минимальное значение S, 
когда такая ситуация возможна"""
# 0 1 2 3 4
# 0 П В П В
def f19(k,p):
    if p==2: return k>=68
    # if p==1 and k>=68: return False
    p += 1
    b1 = f19(k+1,p)
    b2 = f19(k+4,p)
    b3 = f19(k*5,p)
    return b1 or b2 or b3

for s in range(1, 68):
    if f19(s,0):
        print(s)
        break
