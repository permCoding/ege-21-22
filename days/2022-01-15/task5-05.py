''' https://inf-ege.sdamgia.ru/problem?id=8654 '''

n = 999
while n < 10000:
    n += 1
    w = list(map(int, str(n)))
    a = w[0]*w[1]
    b = w[2]*w[3]
    if max(a,b)==12 and min(a,b)==4:
        print(n)
        break