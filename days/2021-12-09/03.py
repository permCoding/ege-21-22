f = open('000.txt')
text = f.read()
f.close()

lst = text.split('\n')

print(lst)
print(lst[0])
print(lst[1])
print(lst[2])
