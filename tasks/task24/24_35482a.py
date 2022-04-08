# https://inf-ege.sdamgia.ru/problem?id=35482
""" найти строку, содержащую наименьшее количество букв G если 
таких строк неск, надо взять ту, которая находится в файле раньше, 
и определить, какая буква встречается в этой строке чаще всего. 
Если таких букв неск, надо взять ту, котор позже стоит в алфав"""

with open("24_35482.txt") as f:
    min_s = min(f.readlines(), key=lambda s: s.count("G"))

alp = [chr(65+i) for i in range(26)][::-1]

lst = [(smb, min_s.count(smb)) for smb in alp]

print(max(lst, key=lambda x: x[1]))
