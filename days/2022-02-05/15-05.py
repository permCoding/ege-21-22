# https://inf-ege.sdamgia.ru/problem?id=37150
R = 333
for a in range(R, -1, -1):
    b = True
    
    for x in range(R):
        for y in range(R):
            f = (70!=2*x+y) or (x<y) or (a<x)            
            if not f:
                b = False
                break
        if b == False:
            break

    if b:
        print(a)
        break
