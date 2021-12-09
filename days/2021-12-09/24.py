f = open('002.txt', 'w')

lines = ['1', '22', '303', '4', '5']

f.writelines(map(lambda x: x+'\n', lines))

f.close()
