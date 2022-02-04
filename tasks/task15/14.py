# https://inf-ege.sdamgia.ru/problem?id=18499

for a in range(0, 200):
    for m in range(0, 200):
        for n in range(0, 200):
            f = (2*m+3*n>40) or ((m<a) and (n<=a))
            if f == False:
                break
        else:
            continue
        break
    else:
        print(a)
        break
