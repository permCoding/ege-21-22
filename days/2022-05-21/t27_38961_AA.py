# https://inf-ege.sdamgia.ru/problem?id=38961
f = open("27-A.txt")
n = int(f.readline())
a = [int(e) for e in f]

mx = 0

for i in range(n):
    for j in range(n):
        lst = list(filter(lambda e: e%2==0, a[i:j+1]))
        if len(lst)%10==0:
            mx = max(mx, sum(a[i:j+1]))

print(mx)
