'''
в первой строке файла записано кол-во натуральных чисел
в последующих N строках файла находятся натуральные числа
найти максимальное число
'''
f = open('001.txt')
lines = f.readlines()
f.close()

n = int(lines[0])
mx = 0
for line in lines[1:n+1]:
    mx = max(mx, int(line))

print(mx)
