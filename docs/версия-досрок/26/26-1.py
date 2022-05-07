f = open("./26-1.txt")
n = int(f.readline())
pairs = [(int(line.split()[0]),int(line.split()[1])) for line in f]
pairs.sort(key=lambda x: (-x[0],+x[1]))

for i in range(n-1):
    if pairs[i][0]==pairs[i+1][0] and pairs[i+1][1]-pairs[i][1]==14: 
        print(pairs[i])

# сортируем по убыванию по колонке 1
# сортируем по возрастанию по колонке 2
# фильтруем колонку 3 до расстоянию+1
# =ЕСЛИ(A3=A2;B3-B2;0)