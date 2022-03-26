# https://inf-ege.sdamgia.ru/problem?id=37162
"""На вход программы поступает последовательность из целых положительных чисел. 
Необходимо выбрать такую подпоследовательность подряд идущих чисел, чтобы 
их сумма была максимальной и делилась на 89, а также её длину. Если таких 
подпоследовательностей несколько, выбрать такую, у которой длина меньше."""

f = open("27_B.txt")
n = int(f.readline())

sm, max_sm, min_ln = 0, 0, n
lst = [0] * 89
pos = [-1] * 89
for i in range(n):
    num = int(f.readline())
    sm += num
    ost = sm%89
    if ost == 0:
        max_sm = sm
        min_ln = i+1
    else:
        if pos[ost] == -1:
            pos[ost] = i
            lst[ost] = sm
        else:
            if sm-lst[ost] == max_sm:
                min_ln = min(min_ln, i-pos[ost])
            if sm-lst[ost] > max_sm:
                max_sm = sm-lst[ost]
                min_ln = i-pos[ost]

f.close()
print(max_sm, min_ln)
