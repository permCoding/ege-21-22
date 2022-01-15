''' https://inf-ege.sdamgia.ru/problem?id=27421
Текстовый файл состоит не более чем из 10^6 символов X, Y и Z. 
Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
'''
line = open('24_7.txt').readline()
# line = 'ZZZZ'
# line = '~' + line
n = len(line)
count, mx = 1, 0
for i in range(n-1):
    if line[i] != line[i+1]:
        count += 1
    else:
        count = 1
    mx = max(mx, count)
print(mx)

