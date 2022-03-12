# 1 чтение данных
with open("./26-demo.txt") as f:
    lines = f.readlines()

# 2 подготовка данных
s, n = map(int, lines[0].split())
nums = sorted(map(int, lines[1:n+1]))

# 3 узнать сколько влезет
sm = 0
for i in range(n):
    if sm + nums[i] > s:
        break
    sm += nums[i]  # sm = sm + nums[i]
print(i)

# 4 найти максим возм элемент
elm = s - sm +  nums[i-1]
for j in range(n-1, i-2, -1):
    if nums[j] <= elm:
        print(nums[j])
        break
