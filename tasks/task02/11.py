# https://inf-ege.sdamgia.ru/problem?id=37137

for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                f = (not a and not b) or (b==c) or d
                if f == False:
                    print(c,d,b,a)
