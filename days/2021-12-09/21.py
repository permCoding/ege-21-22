f = open('002.txt', 'w')

lines = ['1', '2', '3', '4', '5']

lst = []
for line in lines:
    lst.append(line + '\n')

f.writelines(lst)

f.close()
