from random import randint

f = open('data.txt', 'r')

line = f.readline()
print(int(line))

line = f.readline()
print(int(line))

line = f.readline()
print(int(line))

f.close()