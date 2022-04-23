# https://inf-ege.sdamgia.ru/problem?id=35482
""" найти строку, содержащую наименьшее количество букв G если 
таких строк неск, надо взять ту, которая находится в файле раньше, 
и определить, какая буква встречается в этой строке чаще всего. 
Если таких букв неск, надо взять ту, котор позже стоит в алфав"""

lst = [
    ('A', 35),
    ('C', 12),
    ('D', 66),
    ('E', 25),
    ('B', 66),
    ('X', 66)
]

print(lst)
print(max(lst, key=lambda x: x[1]))  # первый встретившийся

lst.sort(key=lambda x: x[0], reverse=True)

print(lst)
print(max(lst, key=lambda x: x[1]))