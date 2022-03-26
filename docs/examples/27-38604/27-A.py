# https://inf-ege.sdamgia.ru/problem?id=38604
""" Дана последовательность из N натуральных чисел. 
Рассматриваются все её непрерывные подпоследовательности, 
такие что сумма элементов каждой из них кратна k=43. 
Найдите среди них подпоследовательность с максимальной суммой, 
определите её длину. Если таких подпоследовательностей найдено несколько, 
в ответе укажите количество элементов самой короткой из них."""

f = open("27_B.txt")
n = int(f.readline())

sm, max_sm, min_ln = 0, 0, n
lst = [0] * 43
pos = [-1] * 43
for i in range(n):
    num = int(f.readline())
    sm += num
    ost = sm%43
    if ost == 0:
        max_sm = sm
        min_ln = i+1
    else:
        if lst[ost] == 0:
            lst[ost] = sm
            pos[ost] = i
        else:
            if sm-lst[ost] == max_sm:
                min_ln = min(min_ln, i-pos[ost])
            if sm-lst[ost] > max_sm:
                max_sm = sm-lst[ost]
                min_ln = i-pos[ost]

print(max_sm, min_ln)
f.close()
