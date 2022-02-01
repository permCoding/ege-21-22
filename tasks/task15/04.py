# https://inf-ege.sdamgia.ru/problem?id=13745

def check(x, y, a):
    return ((x<=9) <= (x*x<=a)) and ((y*y<=a) <= (y<=9))


a = 0
while a < 200:
    a += 1
    
    for x in range(200):
        for y in range(200):
            if check(x, y, a) == False:
                break
        else:
            continue
        break
    else:
        print(a)
        # break
