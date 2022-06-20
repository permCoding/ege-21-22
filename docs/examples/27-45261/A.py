# https://inf-ege.sdamgia.ru/problem?id=45261
# Определите минимальные расходы на доставку мусора

f = open("27_A.txt")
n = int(f.readline())
a = [int(e) for e in f]

mn = 10**12
for i in range(n):
    sm = 0
    for j in range(n):
        dist = min(abs(i-j), n-abs(i-j))
        sm += a[j]*dist
    mn = min(mn, sm)
print(mn)
