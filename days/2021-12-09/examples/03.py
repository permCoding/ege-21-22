from random import randint

file = open('data.txt', 'r')

for line in file:
    print(int(line))

file.close()
