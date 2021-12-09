from random import randint

with open('data.txt', 'w') as f:
    n = 100
    for _ in range(n):
        num = randint(1, 10000)
        f.write(str(num) +'\n')

