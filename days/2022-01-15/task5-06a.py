''' https://inf-ege.sdamgia.ru/problem?id=27232 '''

for n in range(100, 1000):
    s = str(n)
    w = sorted([s[0], s[1], s[2]])
    mx = int(w[2] + w[1])
    mn = int(w[1] + w[0]) if w[0]=='0' else int(w[0] + w[1])
    if mx - mn == 50:
        print(n)
        break
    