# https://inf-ege.sdamgia.ru/problem?id=14217

for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                if z and not(y) and (w<=x):
                    print(z,y,x,w)
