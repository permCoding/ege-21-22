f = open('001.txt')

N = int(f.readline())

mx = 0
for i in range(0, N):
    line = f.readline().strip()
    num = int(line)
    if num > mx:
        mx = num

print(mx)
f.close()
