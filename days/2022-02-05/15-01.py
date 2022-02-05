# https://inf-ege.sdamgia.ru/problem?id=9804

for a in range(200):
    b = True
    for x in range(200):
        f1 = ((x & 29) != 0) 
        f2 = (((x & 17) == 0) <= ((x & a) != 0))
        f = f1 <= f2
        if f == False:
            b = False
            break
    if b:
        print(a)
        break