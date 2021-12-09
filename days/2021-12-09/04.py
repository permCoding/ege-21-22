f = open('000.txt')
text = f.read()
f.close()

lines = text.split('\n')

for line in lines:
    print(line)
