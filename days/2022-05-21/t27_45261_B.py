# https://inf-ege.sdamgia.ru/problem?id=45261
f = open("27_B.txt")
n = int(f.readline())
a = [int(e) for e in f]

mn = 0  # для i==0
for j in range(n):
    dist = min(j, n-j)
    mn += dist*a[j]

_i = n//2
sma = sum(a[_i:])  # половина до завода
smb = sum(a[1:_i])  # половина после завода
sm = mn

for i in range(1, n):
    sma += -a[_i] + a[i-1]
    smb += +a[_i] - a[i]
    sm += sma - smb - a[i]
    _i = (_i+1)%n
    mn = min(mn, sm)

print(mn)
