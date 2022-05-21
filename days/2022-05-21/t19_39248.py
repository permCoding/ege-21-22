# https://inf-ege.sdamgia.ru/problem?id=39248
# +1/*3 | s>=64 | 1<=s<=63
''' S, при котором Петя не может выиграть 
за один ход, но при любом ходе Пети Ваня 
может выиграть своим первым ходом'''
# 0 1 2 3 4
# 0 П В П В

def f(s, h):
    if h==2: return s>=64
    if h==1 and s>=64: return False
    h += 1
    b1 = f(s+1,h)
    b2 = f(s*3,h)
    if h==1: return b1 and b2
    return b1 or b2


for s in range(1, 64):
    if f(s, 0):
        print(s)
        break
