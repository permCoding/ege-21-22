# https://inf-ege.sdamgia.ru/problem?id=28554

for a in range(200, -1, -1):

    bx = True
    for x in range(0, 200):

        by = True
        for y in range(0, 200):
            f = (x*y<140) or (y>a) or (x>a)
            if f == False:
                by = False
                break
        
        if by == False:
            bx = False
            break
    if bx:
        print(a)
        break

