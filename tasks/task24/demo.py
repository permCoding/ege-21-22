with open("./24.txt") as f:
    s = f.readline().strip()

d, m = 0, 0
for i in range(1, len(s)):
    if s[i-1]+s[i] == "PP":
        d = 1
    else:
        d += 1
        m = max(m, d)

print(m)
