from re import findall

for n in range(12345000, 123459999):
    lst = findall(f'^12345.7*8$', str(n))
    if lst!=[]:
        if n%23==0:
            print(n, n//23)
