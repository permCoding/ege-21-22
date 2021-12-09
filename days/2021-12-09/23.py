f = open('002.txt', 'w')

lines = ['111', '2', '303', '4', '5']

def func(x):
    return x + '\n'

f.writelines(map(func, lines))

f.close()
