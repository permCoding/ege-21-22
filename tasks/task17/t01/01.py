f = open('17.txt')
lines = f.readlines()

lst = []
for line in lines:
    lst.append(int(line))

k = 0
s = -20000
for i in range(1, len(lst)):
    a, b = lst[i-1], lst[i]
    if a%3==0 or b%3==0:
        k += 1
        if a+b>s:
            s = a+b
            print(i, a,b,s)
print(k, s)
        
