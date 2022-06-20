# https://inf-ege.sdamgia.ru/problem?id=39250
# +1/*3 | s>=64 | 1<=s<=63
''' S, при котором у Вани:
1) есть выигрышная стратегия, позволяющая ему 
выиграть первым или вторым ходом при любой игре Пети, 
2) нет стратегии, которая позволяла бы ему 
гарантированно выиграть первым ходом'''
# 0 1 2 3 4
# 0 П В П В

def f(s, h):  # 19 21
    if h==4: return s>=64
    if h==2 and s>=64: return True
    if (h==1 or h==3) and s>=64: return False
    h += 1
    b1 = f(s+1,h)
    b2 = f(s*3,h)
    if h==1 or h==3: return b1 and b2
    return b1 or b2


def f_(s, h):  # 21
    if h==2: return s>=64
    if h==1 and s>=64: return False
    h += 1
    b1 = f_(s+1,h)
    b2 = f_(s*3,h)
    if h==1: return b1 and b2
    return b1 or b2


for s in range(1, 64):
    if f(s, 0):
        print(s)

for s in range(1, 64):
    if f_(s, 0):
        print(s)
