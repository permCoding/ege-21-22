'''
в первой строке файла записано кол-во натуральных чисел
в последующих N строках файла находятся натуральные числа
найти максимальное число
'''

f = open('001.txt')

N = int(f.readline())

mx = 0
for i in range(0, N):
    mx = max(mx, int(f.readline()))

print(mx)
f.close()
