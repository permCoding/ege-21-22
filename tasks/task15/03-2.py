# https://inf-ege.sdamgia.ru/problem?id=23916

def check(x, y, a):
    return (x + 2*y < a) or (y > x) or (x > 20)


a = 0
while True:
    a += 1
    
    for x in range(100):
        for y in range(100):
            if check(x, y, a) == False:
                break
        else:
            continue
        break
    else:
        print(a)
        break
