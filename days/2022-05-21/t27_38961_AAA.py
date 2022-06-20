# https://inf-ege.sdamgia.ru/problem?id=38961
f = open("27-A.txt")
n = int(f.readline())
a = [int(e) for e in f]

mx = 0

for i in range(n):
    sm = 0
    for j in range(i, n):
        sm += a[j]
        lst = [e for e in a[i:j+1] if e%2==0]
        if len(lst)%10==0:
            mx = max(mx, sm)

print(mx)
