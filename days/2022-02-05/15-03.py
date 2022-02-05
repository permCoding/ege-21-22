# https://inf-ege.sdamgia.ru/problem?id=34521

a = 200
while a > 0:
    a -= 1

    x = 200
    while x > 0:
        x -= 1

        f = (x&51==0) or ((x&41==0)<=(x&a==0))
        if not f:
            break
    else:
        print(a)
        break
