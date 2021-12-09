from random import randint

n = 100  # кол-во чисел
lines = [str(randint(1, 10000))+'\n' for _ in range(n)]

open('data.txt', 'w').writelines(lines)
