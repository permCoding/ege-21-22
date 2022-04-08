# https://inf-ege.sdamgia.ru/problem?id=36879
"""В строках, содержащих менее 25 букв G, найти макс
расст между одинаковыми буквами в одной строке. """

def get(s):
    r = 0
    for i in range(len(s)):
        smb = s[i]
        pos = s.rfind(smb)
        dist = pos - i
        r = max(r, dist)
    return r


with open("./inf_26_04_21_24.txt") as f:
    lines = f.readlines()
lines = filter(lambda x: x.count("G")<25, lines)
m = 0
for line in lines:
    m = max(m, get(line.strip()))
print(m)
