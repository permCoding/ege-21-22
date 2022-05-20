# https://inf-ege.sdamgia.ru/problem?id=39256

f = open("27-A.txt")
n = int(f.readline())
a = [int(e) for e in f]

mx = 0

for i in range(n):  # 0
    for j in range(i, n):  # 0
        lst = [e for e in a[i:j+1] if e%2==1]
        if len(lst)%10==0:
            mx = max(mx, sum(a[i:j+1]))

print(mx)
