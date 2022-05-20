# https://inf-ege.sdamgia.ru/problem?id=39256

f = open("27-B.txt")
n = int(f.readline())

mx = 0

lst_s = [-1]*10
sm = 0
cnt = 0
for i in range(n):
    num = int(f.readline())
    sm += num
    if num%2==1: cnt += 1
    k = cnt%10
    if k == 0:
        mx = sm
    else:
        if lst_s[k] > -1:
            mx = max(mx, sm-lst_s[k])
        else:
            lst_s[k] = sm

print(mx)