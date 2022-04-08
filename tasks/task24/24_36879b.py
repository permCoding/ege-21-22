# https://inf-ege.sdamgia.ru/problem?id=36879
"""В строках, содержащих менее 25 букв G, найти макс
расст между одинаковыми буквами в одной строке. """

def get(s):
    r = 0
    for i in range(len(s)):
        last = s.rfind(s[i])
        r = max(r, last-i)        
    return r


f = open("./inf_26_04_21_24.txt")
m = 0
while True:
    s = f.readline()
    if not s:
        break
    if s.count("G") < 25:
        m = max(m, get(s.strip()))
print(m)
f.close()
