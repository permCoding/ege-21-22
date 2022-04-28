f = open("./26-1.txt")
n = int(f.readline())
pairs = [(int(line.split()[0]),int(line.split()[1])) for line in f]
pairs.sort(key=lambda x: (-x[0],+x[1]))

for i in range(n-1):
    if pairs[i][0]==pairs[i+1][0] and pairs[i+1][1]-pairs[i][1]==14: 
        print(pairs[i])
