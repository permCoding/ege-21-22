from random import randint

f = open('data.txt', 'w')

n = 100
for _ in range(n):
    num = randint(1, 10000)
    f.write(str(num) +'\n')

f.close()
