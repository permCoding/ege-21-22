# 48661 21040

f = open("t26-1.txt")
n = int(f.readline())
# a = [(int(e.split()[0]), int(e.split()[1])) for e in f]
a = [list(map(int, e.split())) for e in f]

a.sort(key=lambda x: (-x[0], x[1]))

for i in range(n-1):
    if a[i][0]==a[i+1][0] and a[i+1][1]-a[i][1]==14:
        print(a[i][0], a[i][1]+1)
        break
