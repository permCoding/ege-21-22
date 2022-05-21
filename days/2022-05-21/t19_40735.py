# https://inf-ege.sdamgia.ru/problem?id=40735
# +1/+2/*2 | s>=34 | 1<=s<=33
# нельзя потворять
""" S, при котором Петя не может выиграть 
за один ход, но при любом ходе Пети Ваня 
может выиграть своим первым ходом, нельзя 
повторять ход, который только что сделал второй игрок"""

def f(s, h, p):  # p - это какой был ранее ход
    if h==2: return s>=34
    if h==1 and s>=34: return False
    h += 1
    b1 = f(s+1, h, 1)  # p==1
    b2 = f(s+2, h, 2)  # p==2
    b3 = f(s*2, h, 3)  # p==3
    if h==1:
        if p==0: return b1 and b2 and b3  # при любом
        if p==1: return b2 and b3  # ранее был 1
        if p==2: return b1 and b3  # ранее был 2
        if p==3: return b1 and b2  # ранее был 3
    if h==2:
        if p==0: return b1 or b2 or b3  # при любом
        if p==1: return b2 or b3  # ранее был 1
        if p==2: return b1 or b3  # ранее был 2
        if p==3: return b1 or b2  # ранее был 3


for s in range(1, 34):
    if f(s, 0, 0):
        print(s)
