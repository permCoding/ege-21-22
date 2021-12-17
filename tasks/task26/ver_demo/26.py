lines = open('27881.txt').readlines()
s, n = map(int, lines[0].split())
lst = list(sorted(map(int, lines[1:])))

for i in range(len(lst)):
    if sum(lst[:i]) > s:  # взяли лишний
        break

pos = i-1  # убрали номер лишнего
print(pos)  # это позиция последнего взятого
# счёт от нуля, поэтому это кол-во взятых эл-тов
res = sum(lst[:pos-1])
for item in lst[pos:][::-1]:
    if res + item <= s:
        print(item)
        break
