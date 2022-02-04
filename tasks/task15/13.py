# https://inf-ege.sdamgia.ru/problem?id=16821


for a in range(200):
    for x in range(200):
        for y in range(200):
            f = (3*x+4*y!=70) or (a>x) or (a>y)
            if f == False:
                break
        else:
            continue
        break
    else:
        print(a)
        break
