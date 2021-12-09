'''
задание №9 - https://inf-ege.sdamgia.ru/problem?id=38943
Определите сколько среди заданных троек чисел таких, 
которые могут быть сторонами остроугольного треугольника.
'''

k = 0
for line in open('09.csv').readlines():
    lst = sorted(list(map(int, line.split(';'))))
    if lst[2]**2 < lst[0]**2 + lst[1]**2:
        k += 1

print(k)