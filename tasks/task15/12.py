# https://inf-ege.sdamgia.ru/problem?id=16447

for a in range(200, 0, -1):
    for x in range(0, 200):
        for y in range(0, 200):
            f = (2*x+3*y<30) or (x+y>=a)
            if f == False:
                break
        else:
            continue
        break
    else:
        print(a)
        break