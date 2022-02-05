# https://inf-ege.sdamgia.ru/problem?id=14217
# z ∧ ¬y ∧ (w → x) 
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = z and not y and (w<=x)
                if f:
                    print(z,y,x,w)
