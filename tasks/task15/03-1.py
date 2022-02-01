# https://inf-ege.sdamgia.ru/problem?id=23916

def check(x, y, a):
    return (x + 2*y < a) or (y > x) or (x > 20)


for a in range(100):
    bx =True
    for x in range(100):
        by = True
        for y in range(100):
            if check(x, y, a) == False:
                by = False
                break
        if by == False:
            bx = False
            break
    if bx:
        print(a)
        break
        