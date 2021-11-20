'''
Текстовый файл состоит из символов P, Q, R и S.
Определите  максимальное  количество  идущих  подряд  символов
в прилагаемом файле, среди которых нет идущих подряд символов P.
Для выполнения этого задания следует написать программу.
Пример строки:
PRPPPRQSPP
Ответ: 5
'''

line = 'PRP'
line = 'PRPPPRQSPPQSQQSPRQRRRRSSRPSRSSRSSSSPRQRPQRPPQQSSPSP'
# f = open('input.txt')
# line = f.readline()

count, max_count = 1, 1
pred = ''
for smb in line:
    if pred == '':
        pred = smb
        count = 1
    elif pred == smb and pred == 'P':
        count = 1
    else:
        pred = smb
        count += 1
        max_count = max(count, max_count)
print(max_count)
