# https://inf-ege.sdamgia.ru/problem?id=38961
f = open("27-A.txt")
n = int(f.readline())
a = [int(e) for e in f]

mx = 0

for i in range(n):
    sm, cnt = 0, 0
    for j in range(i, n):
        sm += a[j]
        if a[j]%2==0: cnt += 1
        if cnt%10==0: mx = max(mx, sm)

print(mx)
