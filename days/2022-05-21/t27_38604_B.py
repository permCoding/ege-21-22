# https://inf-ege.sdamgia.ru/problem?id=38961
f = open("./27_B_38604.txt")
n = int(f.readline())

mx, ln = 0, 10**20
lst_s = [0]*43  # суммы от 0 по кратностям
lst_p = [0]*43  # суммы от 0 по кратностям
sm0 = 0

for i in range(n):
    ai = int(f.readline())
    sm0 += ai
    k = sm0%43  # кратность 0 1 3 .. 42
    if k==0:
        mx = sm0
        ln = i+1
    else:
        if lst_s[k] == 0:  # первый встретившийся
            lst_s[k] = sm0
            lst_p[k] = i
        else:
            sm = sm0 - lst_s[k]
            lnc = i - lst_p[k]
            if sm == mx:
                ln = min(ln, lnc)
            if sm > mx:
                mx = sm
                ln = lnc

print(mx, ln)
