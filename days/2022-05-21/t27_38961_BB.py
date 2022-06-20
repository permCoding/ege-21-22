# https://inf-ege.sdamgia.ru/problem?id=38961
f = open("27-B.txt")
n = int(f.readline())

mx = 0
lst_s = [0]*10  # суммы от 0 по кратностям
sm0, cnt = 0, 0

for i in range(n):
    ai = int(f.readline())
    sm0 += ai
    if ai%2==0: cnt += 1
    k = cnt%10  # кратность 0 1 3 .. 9
    if k==0:
        mx = sm0
    else:
        if lst_s[k] == 0:  # первый встретившийся
            lst_s[k] = sm0
        else:
            mx = max(mx, sm0-lst_s[k])

print(mx)
