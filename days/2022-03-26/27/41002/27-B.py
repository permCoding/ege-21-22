# https://inf-ege.sdamgia.ru/problem?id=41002
"""Дана последовательность целых чисел. 
Необходимо найти максимально возможную сумму 
её непрерывной подпоследовательности, в которой 
количество положительных нечётных элементов кратно 30.
Первая строка входного файла содержит целое число N — 
общее количество чисел в наборе. Каждая из следующих N 
строк содержит одно число. Гарантируется, что общая сумма 
любой выборки заданных чисел не превышает 2*10**9 по абсолютной величине."""

f = open("./27-B.txt")
n = int(f.readline())

INF = 2*10**9
max_sm = -INF
sm = 0  # сумма от начала списка
cnt = 0  # количество положительных нечётных элементов
lst = [INF] * 30
for i in range(n):
    num = int(f.readline())
    sm += num
    if num>0 and num%2!=0:
        cnt += 1
    ost = cnt%30
    lst[ost] = min(lst[ost], sm)
    max_sm = max(max_sm, sm-lst[ost])

print(max_sm)
f.close()
