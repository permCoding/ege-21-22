# https://inf-ege.sdamgia.ru/problem?id=41002
""" Дана последовательность целых чисел. 
Необходимо найти максимально возможную сумму 
её непрерывной подпоследовательности, в которой 
количество положительных нечётных элементов кратно k=30."""

f = open("./27-A.txt")
n = int(f.readline())

INF = 999999999
lst = [INF] * 30
max_sm = -INF
sm, cnt = 0, 0
for i in range(n):
    x = int(f.readline())
    sm += x
    if x%2!=0 and x>0:
        cnt += 1
    ost = cnt % 30
    lst[ost] = min(lst[ost], sm)
    max_sm = max(max_sm, sm-lst[ost])

print(max_sm)
f.close()
