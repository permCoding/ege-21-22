# https://inf-ege.sdamgia.ru/problem?id=10278

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if (not(x) and z) or (not(x) and not(y) and not(z)):
                print(x,y,z)
