# https://inf-ege.sdamgia.ru/problem?id=45261
# Определите минимальные расходы на доставку мусора

f = open("27_B.txt")
n = int(f.readline())
a = [int(e) for e in f]

mn = 0
for i in range(n):
    dist = min(i, n-i)
    mn += a[i]*dist

_i = n//2
sma = sum(a[_i:])
smb = sum(a[1:_i])
sm = mn

for i in range(1, n):
    sma += -a[_i] + a[i-1]
    smb += +a[_i] - a[i]
    sm += sma - smb - a[i]
    _i = (_i+1)%n
    mn = min(mn, sm)

print(mn)
