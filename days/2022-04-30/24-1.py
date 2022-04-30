# AAACABBBABAAAAAABABACCCC
# __ACAB__AB_____ABABAC___
# __XX__X_____XXX___
# ['','','XX','','','X']
# max len

s = open("./24-1.txt").readline()
s = s.replace('AC', 'X')
s = s.replace('AB', 'X')
cnt, mx = 0, 0
for e in s:
    if e=='X':
        cnt += 1
        mx = max(mx, cnt)
    else:
        cnt = 0
print(mx)