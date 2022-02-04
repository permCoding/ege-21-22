# https://inf-ege.sdamgia.ru/problem?id=28554

for a in range(200, -1, -1):
    for x in range(0, 200):
        for y in range(0, 200):
            f = (x*y<140) or (y>a) or (x>a)
            if f == False:
                break
        else:
            continue
        break
    else:
        print(a)
        break
