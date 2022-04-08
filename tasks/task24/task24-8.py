# https://inf-ege.sdamgia.ru/problem?id=40999
'''файл содержит только заглавные буквы латинского алфавита ABC...Z 
Определ максимальное количество идущих подряд символов, среди 
которых нет ни одной буквы E и при этом не менее трёх букв A'''

line = open('24_8.txt').readline()

lst = line.split('E')
mx = 0
for item in lst:
    if item.count('A') >= 3:
        mx = max(mx, len(item))
print(mx)
