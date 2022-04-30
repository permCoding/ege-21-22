lst_a = '0123456789'
lst_b = [''] + list(lst_a)
for a in lst_a:
    for b in lst_b:
        n = int(f'12345{a}7{b}8')
        if n%23==0:
            print(n, n//23)

