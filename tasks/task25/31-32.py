# https://inf-ege.sdamgia.ru/problem?id=40741
# https://inf-ege.sdamgia.ru/problem?id=41000
'''
Пусть M(N) — сумма двух наибольших различных натуральных делителей 
натурального числа N, не считая самого числа. 
Если у числа N меньше двух таких делителей, то M(N) считается равным 0.
Найдите 5 наименьших натуральных чисел, превышающих 10 000 000, 
для которых 0 < M(N) < 10 000. В ответе запишите найденные значения M(N) 
в порядке возрастания соответствующих им чисел N.
'''
def get_M(n):
    res = []
    for d in range(n//2, 0, -1):
        if n % d == 0:
            res += [d]
            if len(res) == 2:
                break
    return 0 if len(res) < 2 else sum(res)

k = 0
# i = 10000000
i = 11000000
while k < 5:
    i += 1
    M = get_M(i)
    if 0 < M < 10000:
        print(i, M)
        k += 1