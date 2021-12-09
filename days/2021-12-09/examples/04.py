from random import randint

file = open('data.txt', 'r')

sum_odd = 0
for line in file:
    num = int(line)
    if num % 2 != 0:
        sum_odd += num
        print(num)
print(sum_odd)

file.close()
