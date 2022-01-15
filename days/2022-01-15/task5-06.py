''' https://inf-ege.sdamgia.ru/problem?id=27232 '''

for n in range(100, 1000):
    if n % 100 == 0: continue
    w = sorted(map(int, str(n)))
    mx = w[-1]*10 + w[-2]
    mn = w[1]*10 + w[0] if w[0]==0 else w[0]*10 + w[1]
    if mx - mn == 50:
        print(n)
        break