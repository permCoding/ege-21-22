# https://inf-ege.sdamgia.ru/problem?id=14688

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (x or y) <= (z==x)
            if not f:
                print(x,z,y)
