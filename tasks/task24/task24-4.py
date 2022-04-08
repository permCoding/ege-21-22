# https://inf-ege.sdamgia.ru/problem?id=27421
# https://inf-ege.sdamgia.ru/problem?id=27690
'''файл состоит не более чем из 10^6 символов X, Y и Z. 
Определите максимальное кол-во идущих подряд символов, 
среди которых каждые два соседних различны.'''
# f = open('24-4.txt')
f = open('./24_27690.txt')
line = f.readline()

count, mcount = 1, 0
for i in range(1, len(line)):
    if line[i-1] == line[i]:
        count = 1
    else:
        count += 1
    if count > mcount:
        mcount = count
print(mcount)
