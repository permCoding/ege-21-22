# https://inf-ege.sdamgia.ru/problem?id=35482
""" найти строку, содержащую наименьшее количество букв G если 
таких строк неск, надо взять ту, которая находится в файле раньше, 
и определить, какая буква встречается в этой строке чаще всего. 
Если таких букв неск, надо взять ту, котор позже стоит в алфав"""

f = open("24_35482.txt")
min_s, min_g = "", 999999999
for s in f:
    if s.count("G") < min_g:
        min_g = s.count("G")
        min_s = s
f.close()

alp = [chr(65+i) for i in range(26)][::-1]
mx_smb, cnt = " ", 0
for smb in alp:
    if min_s.count(smb) > cnt:
        cnt = min_s.count(smb)
        mx_smb = smb
print(cnt, mx_smb)
