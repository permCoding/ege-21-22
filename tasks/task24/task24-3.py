'''
https://inf-ege.sdamgia.ru/problem?id=27421
Текстовый файл состоит не более чем из 10^6 символов X, Y и Z. 
Определите максимальное кол-во идущих подряд символов, 
среди которых каждые два соседних различны.
Пример строки:
YYXYZXX
Ответ: 5
'''

line = 'YYXYZXX'

count = 1
mcount = 0
for i in range(1, len(line)):
    if line[i-1] == line[i]:
        count = 1
    else:
        count += 1
    if count > mcount:
        mcount = count
print(mcount)
