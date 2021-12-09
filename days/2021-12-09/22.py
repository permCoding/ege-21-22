f = open('002.txt', 'w')

lines = ['1', '2', '3', '44', '5']

lst = [line+'\n' for line in lines]

f.writelines(lst)

f.close()
