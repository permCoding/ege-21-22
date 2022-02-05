# https://inf-ege.sdamgia.ru/problem?id=37150
for a in range(500, -1, -1):
    for x in range(500):
        for y in range(500):
            f = (2*x+y!=70) or (x<y) or (a<x)
            if f == False:
                break
        else:
            continue
        break
    else:
        print(a)
        break
            
            