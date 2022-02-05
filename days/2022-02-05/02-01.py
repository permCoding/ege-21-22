# https://inf-ege.sdamgia.ru/problem?id=9752

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f1 = (not x and y and z)
            f2 = (not x and not y and z)
            f3 = (not x and not y and not z)
            f = f1 or f2 or f3
            if f:
                print(z,x,y)