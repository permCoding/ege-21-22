# https://inf-ege.sdamgia.ru/problem?id=9804

def f(x,a):
    return ((x&29)!=0)<=(((x&17)==0)<= (x&a!=0))


for a in range(200):
    for x in range(200):
        if not f(x,a):
            break
    else:
        print(a)
        break
