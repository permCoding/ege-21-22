'''
Текстовый файл состоит из символов P, Q, R и S.
Определите  максимальное  количество  идущих  подряд  символов
в прилагаемом файле, среди которых нет идущих подряд символов P.
Для выполнения этого задания следует написать программу.
Пример строки:
PRPPPRQSPP
Ответ: 5
'''
f = open('24.txt')
line = f.readline()

count = 0
mcount = 0
for i in range(1, len(line)):
    if line[i-1] == line[i] == 'P':
        count = 1
    else:
        count += 1
    if count > mcount:
        mcount = count
print(mcount)
