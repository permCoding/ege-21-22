lines = open('9.csv').readlines()
k = 0
for line in lines:
    a,b,c = map(int, line.split(';'))
    if a<b+c and b<a+c and c<a+b:
        k += 1
print(k)