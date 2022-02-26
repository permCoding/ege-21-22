from random import randint

a,b = -100000, +100000
k = randint(-500, +500)
n = 10000
lst = sorted(set([randint(a,b) for _ in range(n)]))

f = open('input.txt', 'w')
f.write(str(k) + '\n')
f.write(str(len(lst)) + '\n')
f.write(' '.join(map(str, lst)))
f.close()
