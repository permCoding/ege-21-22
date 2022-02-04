# https://inf-ege.sdamgia.ru/problem?id=16045

for a in range(500, 0, -1):
    for x in range(1, 500):
        for y in range(1, 500):
            f = (y + 2*x != 48) or (a < x) or (a < y)
            if f == False:
                break
        else:
            continue
        break
    else:
        print(a)
        break
