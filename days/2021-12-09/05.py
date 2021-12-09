f = open('000.txt')
text = f.read()
f.close()

lines = text.split('\n')

for index in range(0, len(lines)):  # правая граница не входит
    print(lines[index])
