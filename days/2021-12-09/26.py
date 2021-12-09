import random

f = open('data.txt', 'w')

n = 100
for _ in range(n):
    num = random.randint(1, 10000)
    f.write(str(num) +'\n')

f.close()
