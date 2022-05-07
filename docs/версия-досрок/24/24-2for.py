"""Найдите максимальное количество подряд идущих 
пар символов CA или CB. Искомая подстрока может 
включать только пары CA, только пары CB или 
содержать одновременно как пары CA, так и пары CB."""
s = open("./24-2.txt").readline().strip()

s = s.replace("CA", "X")
s = s.replace("CB", "X")

mx, cnt = 0, 0
for e in s:
    if e=="X":
        cnt += 1
        mx = max(mx, cnt)
    else:
        cnt = 0
print(mx)
