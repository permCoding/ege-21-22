# https://inf-ege.sdamgia.ru/problem?id=27686
# Определите длину самой длинной последовательности, состоящей из символов X

f = open("./24_9.txt")
s = f.readline()
f.close()

mx, ln = 0, 0
for i in range(0, len(s)):
    if s[i] == 'X':
        ln += 1
        mx = max(mx, ln)
    else:
        ln = 0
print(mx)
