f = open("./27_B.txt")
n = int(f.readline())

sm = 0  # сумма элементов от начала списка
max_sm, min_ln = 0, n
lst = [-1] * 43  # суммы для соответствующих остатков
pos = [-1] * 43  # мин возм позиции для этих сумм
for i in range(n):
    num = int(f.readline())
    sm += num  # сумма эл-тов до текущей i-той позиции
    ost = sm%43
    if ost==0:
        max_sm = sm
        min_ln = i+1
    else:
        if lst[ost]==-1:
            lst[ost] = sm
            pos[ost] = i
        else:
            if sm-lst[ost] == max_sm:
                min_ln = min(min_ln, i-pos[ost])
            if sm-lst[ost] > max_sm:
                max_sm = sm-lst[ost]
                min_ln = i-pos[ost]

print(min_ln)
f.close()
