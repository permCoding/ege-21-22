# https://inf-ege.sdamgia.ru/problem?id=27689
"""файл из X, Y, Z. найдите максим длину цепочки вида XYZXYZXYZ 
составленной из фрагментов XYZ, последний фрагмент может быть неполным"""

s = open("./24_XYZ.txt").readline().strip()

a = "XYZ"
pos, mx = 0, 0
for i in range(len(s)):
    if s[i] == a[pos%3]:
        pos += 1
    else:
        mx = max(mx, pos)
        pos = 0

print(mx)

