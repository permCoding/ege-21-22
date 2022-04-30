
for n in range(1, 100):
    b = bin(n)[2:]
    if n%2==0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    if int(b,2) > 88:
        print(n)
        break
