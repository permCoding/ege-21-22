'''
Текстовый файл состоит из символов P, Q, R и S.
Определите максимальное кол-во идущих подряд символов
в прилагаемом файле,
среди которых нет идущих подряд символов P.
PP => 1
QPPRS => 3
PPPPQRPPPPPPPPSPPPPPP => 3

PP => 1
PR => +1
RR => +1
'''
# line = 'PPQRQRQRSPPRS'

#f = open('24.txt')
#line = f.readline()

line = open('24.txt').readline()

count, max_count = 1, 1
for i in range(1, len(line)):
    # if line[i-1] == line[i] and line[i] == 'P':
    if line[i-1] == line[i] == 'P':
        if count > max_count:
            max_count = count
        count = 1
    else:
        count += 1
        
print(max_count)

# if x < y < z:























